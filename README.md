[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/P1_PdvCS)
# assignment-0-install

# TASK 2
Maze Generation as a search Problem:
A state is an array of cells and a location (a tuple of 2 numbers). Each cell has four sides that are either walls or not walls. The start state is an array of cells where each one has a wall on all four sides and a random location in the maze. The goal state is a state where the outer edges of the array are all walls and for every square, there is a way to get there from every other square moving left, right, up or down and never passing through a wall. The actions are to move left, right, up, or down from the given cell and erase the wall being moved through. The transitions are from the current state to a new state with the location shifted up, down, left, or right and the wall inbetween erased as there is a wall to erase in that direction. 


# TESTS
To the function _check_maze I added:
1. A test checking that the path is valid, meaning that each step is one transition from the previous step (no moving thorugh walls or taking more than one step at a time).
2. A test checking that there are no duplicate states in the path.

Tests I added:
1. checking that bfs and dfs find the right path when the start state is the goal state.
2. checking that bfs and dfs can find the right path when there is only one way to go 
by creating a maze with a height of one and another maze with a width of one.
3. tested that bfs finds the shortest path when there are multiple ways to go in a directed graph.
4. Tested that bfs and dfs return none whent here is no solution.


Collaborators:
Bhavani Venkatesan: Bounced ideas off each other. Helped set up VS workspace.