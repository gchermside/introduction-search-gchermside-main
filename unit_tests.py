import unittest

from maze import Maze
from directed_graph import DirectedGraph #I added this so I could test with directed_graphs
from search import bfs, dfs

class IOTest(unittest.TestCase):
    """
    Tests IO for bfs and dfs implementations. Contains basic/trivial test cases.

    Each test instatiates a Maze object and tests the bfs and dfs algorithms on it.
    Note: The tests currently are only testing if the algorithms start and end at the
    correct locations and if the path returned is the correct length (optional).

    You may wish to add path validity checks. How do you know if a path is valid nor not?
    Your path should not teleport you, move through a wall, or go through a cell more than once.
    Maybe you should test for this... We certainly will during grading!

    These tests are not exhaustive and do not check if your implementation follows the
    algorithm correctly. We encourage you to create your own tests as necessary.
    """

    def _check_maze(self, algorithm, maze, length=None):
        """
        Test algorithm on a Maze
        algorithm: algorithm to test
        maze: Maze to test algorithm on
        length: length that the path returned from algorithm should be.
                Think about why this argument is optional, and when you should provide it.
        """
        def path_is_valid(cur_path):
            """"checks that the cur_path onlt takes valid moves 
            (only moves up, down. left, or right by 1 and does't move through walls)"""
            while len(cur_path) > 1:
                cur_position = cur_path.pop(0)
                succsessors = maze.get_successors(cur_position)
                if cur_path[0] not in succsessors:
                    return False
            return True

        path = algorithm(maze)[0]
        self.assertEqual(path[0], maze.get_start_state(),
                         "Path should start with the start state")
        self.assertTrue(maze.is_goal_state(path[-1]),
                        "Path should end with the goal state")
        if length:
            self.assertEqual(len(path), length,
                             f"Path length should be {length}")
        self.assertEqual(len(path), len(set(path)),
                         "Path should not contain duplicate elements")
        self.assertTrue(path_is_valid(path),
                        "Path should only take valid moves")

    def test_bfs_on_maze(self):
        single_cell_maze = Maze(1, 1)
        self._check_maze(bfs, single_cell_maze, 1)

        two_by_two_maze = Maze(2, 2)
        self._check_maze(bfs, two_by_two_maze, 3)

        large_maze = Maze(10, 10)
        self._check_maze(bfs, large_maze)

        start_at_goal_maze = Maze(6, 4, (3, 2), (3, 2))
        self._check_maze(bfs, start_at_goal_maze, length=0)

        tall_maze = Maze(1, 6)
        self._check_maze(bfs, tall_maze)

        wide_maze = Maze(4, 1)
        self._check_maze(bfs, wide_maze)

        diff_start_and_goal = Maze(4, 4, start=(2, 2), goal=(1, 0))
        self._check_maze(bfs, diff_start_and_goal)

        diff_start_and_goal_wide = Maze(4, 1, start=(0, 0), goal=(0, 3))
        #Maze is passed width, height but start and goal are represented with (row, col)
        self._check_maze(bfs, diff_start_and_goal_wide)

    def test_bfs_and_dfs_on_directed_graph(self):
        two_by_two_graph = DirectedGraph([[None, 1], [None, None]], {1})
        self._check_maze(bfs, two_by_two_graph)
        self._check_maze(dfs, two_by_two_graph)

        #checks that BFS finds the shortest path when there are multiply solutions
        mulit_solution_paths_graph = DirectedGraph([
            [None, 1, 1, 1], 
            [None, None, 1, 1], 
            [None, None, None, 1],
            [None, None, None, None]
        ], {3}, start_state=0)
        self._check_maze(bfs, mulit_solution_paths_graph, length=2)
        self._check_maze(dfs, mulit_solution_paths_graph)

        mulit_solution_paths_graph2 = DirectedGraph([
            [1, None, 1, 1], 
            [None, 1, 1, 1], 
            [None, 1, 1, 1],
            [1, None, 1, 1]
        ], {1}, start_state=0)
        self._check_maze(bfs, mulit_solution_paths_graph2, length=3)
        self._check_maze(dfs, mulit_solution_paths_graph2)

        fully_connected_graph = DirectedGraph([
            [1, 1, 1, 1], 
            [1, 1, 1, 1], 
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ], {2}, start_state=3)
        self._check_maze(bfs, fully_connected_graph, length=2)
        self._check_maze(dfs, fully_connected_graph)

        #testing when there is no solution:
        no_solution_graph = DirectedGraph([
            [None, None, 1, 1], 
            [None, None, 1, 1], 
            [None, None, None, 1],
            [None, None, None, None]
        ], {1}, start_state=0)
        no_path, _ = bfs(no_solution_graph)
        self.assertEqual(no_path, None)        

        no_solution_graph2 = DirectedGraph([
            [None, None, None, 1], 
            [None, None, 1, 1], 
            [None, None, None, 1],
            [None, None, 1, 1]
        ], {1}, start_state=0)
        no_path2, _ = bfs(no_solution_graph2)
        self.assertEqual(no_path2, None)        


    def test_dfs_on_maze(self):
        single_cell_maze = Maze(1, 1)
        self._check_maze(dfs, single_cell_maze, 1)

        two_by_two_maze = Maze(2, 2)
        self._check_maze(dfs, two_by_two_maze, 3)

        large_maze = Maze(10, 10)
        self._check_maze(dfs, large_maze)
      
        start_at_goal_maze = Maze(6, 4, (3, 2), (3, 2))
        self._check_maze(dfs, start_at_goal_maze, 0)

        tall_maze = Maze(1, 4)
        self._check_maze(dfs, tall_maze, 4)

        wide_maze = Maze(2, 1)
        self._check_maze(dfs, wide_maze, 2)

        diff_start_and_goal = Maze(4, 4, start=(2, 2), goal=(1, 0))
        self._check_maze(dfs, diff_start_and_goal)

        diff_start_and_goal_wide = Maze(4, 1, start=(0, 0), goal=(0, 3))
        #Maze is passed width, height but start and goal are represented with (row, col)
        self._check_maze(dfs, diff_start_and_goal_wide, 4)



if __name__ == "__main__":
    unittest.main()
