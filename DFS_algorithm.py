'''
DFS Algorithm Implementation

'''
import math
import numpy as np
import random as rn
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys
from maze_generation import generate_maze

'''
Notes:

stack.pop() and stack.append() work the same but reversed due to stack being represented as a list: append puts item at the end, pop removes from the end

'''

'''Main function'''
def dfs_find_path(maze_array, start,goal):
    # Initialize stack with the start position and the visited list
    stack = [start]
    visited = [] 

    while len(stack) != 0:
        # Get position at top of the stack as the current cell
        position = stack.pop()
        row, item = position

        # Return the path if the goal is reached
        if position == goal:
            visited.append(position)
            return visited
        
        # Add cell as visited
        visited.append((row,item))

        # Explore neighbors
        for d_row, d_item in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_item = row + d_row, item + d_item
        
            # Check if within bounds, if cell is already visited or is not carved path 
            if (0 <= new_row < len(maze_array) and 0 <= new_item < len(maze_array[0])) and (maze_array[new_row][new_item] == 1 or maze_array[new_row][new_item] == 2 or maze_array[new_row][new_item] == 4)  and (new_row, new_item) not in visited:
                stack.append((new_row, new_item))

    return [] # Return nothing is no path is found

if __name__ == "__main__":
    maze_array, start, goal = generate_maze(10,5)

    print()

    '''print(start)
    print(goal)
    print(maze_array)'''

    path = dfs_find_path(maze_array, start, goal)
    print(path)
