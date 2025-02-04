import random
import argparse
from typing import Dict
from maze import Maze, MazeState, MazeRoom
from search_problem import SearchProblem
from search import dfs, bfs


############### TASK 3 EXTRA CREDIT ###############
class MazeGenerator(SearchProblem[MazeState]):
    """
    Generates a maze as a search problem 

    This class initializes a maze with walls surrounding every cell. The maze 
    generation process can be driven by applying search algorithms like BFS or DFS, 
    which explore the maze and create paths by visiting cells and removing walls. 
    It keeps track of the visited cells and checks when all cells have been 
    visited (i.e., when the maze is fully generated).

    Attributes:
        width (int): The width of the maze in terms of the number of cells.
        height (int): The height of the maze in terms of the number of cells.
        board (Tuple[Tuple[MazeRoom]]): A 2D list representing the maze grid where each cell is a MazeRoom.
        start_state (MazeState): The starting state of the maze, where the generation begins.
        visited_cells_count (int): The count of cells that have been visited during maze generation.
        total_cells (int): The total number of cells in the maze.
    """
    def __init__(self, width: int, height: int):
        """
        Initializes the maze generator with a given width and height.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.
        """
        self.width = width
        self.height = height
        
        # Initialize the maze grid with walls everywhere
        self.board = self.board = [[MazeRoom() for _ in range(width)] for _ in range(height)]

        # Start at a random location within the maze
        start_x, start_y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        
        # Start the starting cell of the board as visited to be True
        self.board[start_x][start_y].visited = True

        # Set the initial start state and initialize the counters for the maze generation process
        self.start_state = MazeState(self.board, (start_x, start_y)) 
        self.visited_cells_count = 1  # Start with the initial cell visited
        self.total_cells = self.width * self.height   # Total number of cells in the maze

    def get_start_state(self) -> MazeState:
        """
        Returns the start state of the maze.

        This method retrieves the initial starting state of the maze, which is
        typically used as the entry point for maze generation or solving algorithms.

        Returns:
            MazeState: The initial state of the maze.
        """
        return self.start_state
        
    def is_goal_state(self, state: MazeState) -> bool:
        """
        Determines whether the goal state of the maze has been reached.

        This method checks if all cells in the maze have been visited, indicating
        that the maze generation or solving process is complete.

        Args:
            state (MazeState): The current state of the maze.

        Returns:
            bool: True if all cells have been visited and the goal state is reached,
                False otherwise.
        """
        if self.total_cells == self.visited_cells_count:
            return True
        return False


    def get_successors(self, state: MazeState) -> set[MazeState]:
        """
        Generates the successor states from the current state in the maze.

        This method explores the possible moves from the current state by checking 
        adjacent cells in the four cardinal directions (north, south, east, west). 
        It only considers cells that have not been visited and are within the maze's 
        boundaries. When a valid move is found, the wall between the current cell 
        and the adjacent cell is removed, and the adjacent cell is marked as visited.

        Args:
            state (MazeState): The current state of the maze.

        Returns:
            set[MazeState]: A set of successor MazeState objects.
        """
        successors = set()
        directions = ['north', 'south', 'east', 'west']
        random.shuffle(directions) #doesn't move the same directions every maze generated
        while directions:
            start_row, start_col = state.location
            for direction in directions:
                new_row, new_col = self.get_row_and_col(start_row, start_col, direction)
                if self.is_in_range(new_row, new_col): 
                    if state.board[new_row][new_col].visited is not True:
                        #if we can move to a new, in-range MazeRoom: update the board to remove the wall
                        # from both cells and increase visited_cells_count
                        setattr(self.board[start_row][start_col], direction, 0)
                        setattr(self.board[new_row][new_col], self.opposite_direction(direction), 0)
                        self.board[new_row][new_col].visited = True
                        self.visited_cells_count += 1
                        new_maze_state = MazeState(state.board, (new_row, new_col))
                        successors.add(new_maze_state)
            return successors

    def get_row_and_col(self, start_row: int, start_col: int, direction: str) -> tuple[int, int]:
        """
        returns a new location, moved according to direction
        Args:
            start_row int: the current row location
            start_col int: the current colum location
            dirction (string): a cardinal direction(north, east, south, west) by which to move

        Return:
            a new location shifted 1 by direction
        """
        if direction == "north":
            return (start_row - 1, start_col)
        if direction == "south":
            return (start_row + 1, start_col)
        if direction == "west":
            return (start_row, start_col - 1)
        if direction == "east":
            return (start_row, start_col + 1)
        raise Exception("get_row_and_col not passed a valid direction")


# /////////////////////////////// Don't Edit Beyond this Line! /////////////////////////////////////

    def is_in_range(self, row: int, col: int) -> bool:
        """
        Checks whether a given position is within the bounds of the maze.

        This method verifies if the specified row and column indices fall within 
        the valid range of the maze's dimensions.

        Args:
            row (int): The row index to check.
            col (int): The column index to check.

        Returns:
            bool: True if the position is within the maze's boundaries, False otherwise.
        """
        return 0 <= row < self.height and 0 <= col < self.width

    def opposite_direction(self, direction: str) -> str:
        """
        Returns the opposite direction of the given direction.

        This method maps a given cardinal direction (north, south, east, west) 
        to its opposite direction.

        Args:
            direction (str): The direction for which the opposite is needed.

        Returns:
            str: The opposite direction.
        """
        opposites = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
        return opposites[direction]


def main():
    """
    Main function to generate and solve a maze using BFS and DFS algorithms.
    """  
    parser = argparse.ArgumentParser(description='Run maze generator')
    parser.add_argument('--size', type=int, default=5, help='Size of the TileGame (default: 5)')

    args = parser.parse_args()
    SIZE = args.size

    # Create Maze Generator
    generator = MazeGenerator(SIZE, SIZE)

    print("bfs maze generation")
    # Perform BFS to explore and generate the maze structure
    bfs_result = bfs(generator)
    bfs_path = bfs_result[0]  # Extract the list of MazeState objects from the result
    print(bfs_path)

    # Visualize the final state in BFS path
    if bfs_path:
        bfs_maze = Maze(generator.width, generator.height, board=bfs_path[-1].board) 
        bfs_maze.visualize_maze(algorithm_name="bfs")

        # Run BFS to solve maze
        print("BFS Path:")
        bfs_path, bfs_stats = bfs(bfs_maze)
        bfs_maze.visualize_maze(path=bfs_path, algorithm_name="bfs")

    generator = MazeGenerator(SIZE, SIZE)

    # Run DFS to generate a maze
    print("dfs maze generation")
    dfs_result = dfs(generator)
    print("dfs_result", dfs_result)
    dfs_path = dfs_result[0]  # Extract the path from the result
    print(dfs_path)

    # Visualize the final state in DFS path
    if dfs_path and isinstance(dfs_path[-1], MazeState):
        dfs_maze = Maze(generator.height, generator.width, board=dfs_path[-1].board) 
        dfs_maze.visualize_maze(algorithm_name="dfs")

        # Run DFS to solve maze
        print("DFS Path:")
        dfs_path, dfs_stats = dfs(dfs_maze)
        dfs_maze.visualize_maze(path=dfs_path, algorithm_name="dfs")


if __name__ == "__main__":
    main()
