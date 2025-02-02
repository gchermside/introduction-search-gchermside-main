[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/P1_PdvCS)
# assignment-0-install

# TASK 2
In your README, describe maze generation as a basic search problem. What are the states, actions, and transitions? What are the start and goal states?

To generate a perfect maze: 
- A state is an array of cells and a location (a tuple of 2 numbers). Each cell has four sides that are either walls or not walls. 
- the start state is a random square on the maze
- the tranisitions are all the adjacent cells(left, right, up, or down) that have walls.
- 


# TESTS

JUST TRASH I COULDN"T DELETE:
    def generate_multi_solution_board(self, walls_to_remove):
        """Generates the maze by randomly carving out paths using the drunken walk algorithm. Then removes extra walls"""
        # Start generating the maze from a random start position
        start_x, start_y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
        self.drunken_walk(start_y, start_x)
        for i in range(0, walls_to_remove):
            row = random.randint(0, self.height - 1)
            col = random.randint(0, self.width - 1)
            directions = ['north', 'south', 'east', 'west']
            random.shuffle(directions)  # Shuffle directions to ensure randomness
            direction = directions.pop()
            for direction in directions:
                nx, ny = col, row
                if direction == 'north':
                    ny -= 1
                elif direction == 'south':
                    ny += 1
                elif direction == 'east':
                    nx += 1
                elif direction == 'west':
                    nx -= 1
            if self.is_in_bounds(ny, nx):
                print()
                setattr(self.board[row][col], direction, 0)
        self.visualize_maze(algorithm_name="in maze")



Collaborators: