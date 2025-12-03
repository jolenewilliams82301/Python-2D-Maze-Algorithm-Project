"""
File: DFS_algorithm.py
Author: Jolene Williams
Description: DFS Algorithm implementation
NCLab Capstone Project 1
Notes:
-- stack.pop() and stack.append() work the same 
but reversed due to stack being represented as a list: 
append puts item at the end, pop removes from the end

"""

from maze_generation import generate_maze


def dfs_find_path(maze_array, start, goal):
    ''' Main DFS function. Solve maze with DFS and return solution path

        Keyword arguments:
        maze_array -- 2d numpy array representing maze
        start -- the start position
        goal -- the goal position
    '''
    # Initialize stack with the start position and the visited list
    stack = [(start, [start])]
    visited = set()
    
    while len(stack) != 0:

        # Get position at top of the stack as the current cell
        position, path = stack.pop()
        row, item = position

        # Return the path if the goal is reached
        if position == goal:
            return path
        
        # Add cell as visited
        visited.add((row,item))

        # Explore neighbors
        for d_row, d_item in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            new_row, new_item = row + d_row, item + d_item
        
            # Check if within bounds, if cell is not visited and is carved path 
            if (0 <= new_row < len(maze_array) and 0 <= new_item < len(maze_array[0])) and (maze_array[new_row][new_item] in {1,2,4})  and (new_row, new_item) not in visited:
                stack.append(((new_row, new_item), path + [(new_row, new_item)]))

    return [] # Return nothing is no path is found

if __name__ == "__main__":
    # For testing
    maze_array, start, goal = generate_maze(5,5)

    print()

    path = dfs_find_path(maze_array, start, goal)
    print(maze_array)
    print(path)
