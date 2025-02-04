from typing import List, Tuple, Dict
from queue import Queue  
from search_problem import SearchProblem, State
from maze import Maze


def bfs(problem: SearchProblem[State]) -> Tuple[List[State], Dict[str, int]]:
    """
    Performs Breadth-First Search (BFS) on the given problem.

    Args:
        problem (SearchProblem[State]): The search problem to solve.

    Returns:
        Tuple[Optional[List[State]], Dict[str, int]]:
            - A list of states representing the solution path, or None if no solution was found.
            - A dictionary of search statistics, including:
                a. 'path_length': The length of the final path.
                b. 'states_expanded': The number of states expanded during the search.
                c. 'max_frontier_size': The maximum size of the frontier during the search.
    """
    stats = {"path_length": 0, "states_expanded": 0, "max_frontier_size": 0}
    paths_queue = [[problem.get_start_state()]]
    visited = [problem.get_start_state()]
    while(len(paths_queue) > 0):
        cur_path = paths_queue.pop(0)
        if problem.is_goal_state(cur_path[-1]): #if the end of the current path is the goal
            stats["path_length"] = len(cur_path)
            #cur_path if the number of squares visted, so the path length is one less because it is the number of lines between points
            return (cur_path, stats)
        else:
            successors = problem.get_successors(cur_path[-1])
            for successor in successors:
                if successor not in visited:
                    new_path = cur_path + [successor]
                    paths_queue.append(new_path)
                    visited.append(successor)
            stats["states_expanded"] = stats["states_expanded"] + 1
            stats["max_frontier_size"] = max(stats["max_frontier_size"], len(paths_queue))
    return None, stats



def dfs(problem: SearchProblem[State]) -> tuple[List[State], Dict[str, int]]:
    """
    Performs a depth-first search (DFS) on the given search problem.

    Args:
        problem (SearchProblem[State]): The search problem to solve.

    Returns:
        Tuple[Optional[List[State]], Dict[str, int]]:
            - A list of states representing the solution path, or None if no solution was found.
            - A dictionary of search statistics, including:
                a. 'path_length': The length of the final path.
                b. 'states_expanded': The number of states expanded during the search.
                d. 'max_frontier_size': The maximum size of the frontier during the search.
    """
    stats = {"path_length": 0, "states_expanded": 0, "max_frontier_size": 0}
    paths_queue = [[problem.get_start_state()]]
     #visited stores all states that have been added to the paths_queue 
     # (even if they have not yet been removed from paths_queue)
    visited = [problem.get_start_state()]
    while(len(paths_queue) > 0):
        cur_path = paths_queue.pop(-1)
        if problem.is_goal_state(cur_path[-1]): #if the end of the current path is the goal
            stats["path_length"] = len(cur_path)
            return (cur_path, stats)
        else:
            successors = problem.get_successors(cur_path[-1])
            stats["states_expanded"] = stats["states_expanded"] + 1
            for successor in successors:
                if successor not in visited:
                    new_path = cur_path + [successor]
                    paths_queue.append(new_path)
                    visited.append(successor)
            stats["max_frontier_size"] = max(stats["max_frontier_size"], len(paths_queue))
    return None



def reconstruct_path(path: Dict[Tuple[int, int], Tuple[int, int]], end: State, problem: SearchProblem[State]) -> List[State]:
    """
    Reconstructs the path from the start state to the given end state.

    Args:
        path (Dict[Tuple[int, int], Tuple[int, int]]): A dictionary mapping each state 
        to its predecessor in the search.
        end (State): The goal state to trace back from.
        problem (SearchProblem[State]): The search problem to solve.

    Returns:
        List[State]: The reconstructed path from the start state to the goal state.
    """
    reverse_path = []
    while end != problem.get_start_state():
        reverse_path.append(end)
        end = path[end]
    reverse_path.append(problem.get_start_state())
    reverse_path.reverse()
    return reverse_path

############### SANDBOX ###############
def main():
    # Initialize the maze and generate it based on given dimensions
    print("Generated Maze:")
    width, height = 10, 5
    maze = Maze(width, height)

    # Run BFS to find paths
    bfs_path, bfs_stats = bfs(maze)
    print("bfs_path ", bfs_path)
    print("bfs_stats ", bfs_stats)
    # maze.visualize_maze(path=bfs_path, algorithm_name="bfs")

    # Run DFS to find paths
    print("DFS Path:")
    dfs_path, dfs_stats = dfs(maze)
    print(dfs_path)
    print("dfs_stats ", dfs_stats)
    # maze.visualize_maze(path=dfs_path, algorithm_name="dfs")


if __name__ == "__main__":
    main()
