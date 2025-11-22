'''
Jolene Williams

Maze Generation

Notes:

In Numpy 2D array representing the maze, 0 is wall, 1 is a carved path

'''
import math
import numpy as np
import random as rn
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys


'''Helper Functions'''

def generate_maze_array(H,W):
    '''Generate maze array (2D numpy array) with H rows each with length W'''
    return np.zeros( (H,W), dtype=np.uint8)


def generate_unvisited_neighbors(row, item, maze_height, maze_width, visited):
    '''Generate list of unvisited neighbors of position (row, item)'''
    unvisited = []
        
    if row > 1 and (row - 2, item) not in visited:
        unvisited.append('NORTH')
    if (row < maze_height - 2) and (row + 2, item) not in visited:
        unvisited.append('SOUTH')
    if (item > 1) and (row, item - 2) not in visited:
        unvisited.append('WEST')
    if (item < maze_width - 2) and (row, item + 2) not in visited:
        unvisited.append('EAST')
    
    return unvisited


def visit(maze_array, visited, maze_height, maze_width):
    '''Randomly generate a maze of size (maze_height x maze_width) using iteration'''
    for (row, item) in visited:
        # Generate list of unvisited neighbors for each position marked as visited
        unvisited = generate_unvisited_neighbors(row, item, maze_height, maze_width, visited)

        if unvisited:
            
            # randomly choose an unvisited neighbor and carve an empty space
            next_intersection = rn.choice(unvisited)
            
            if next_intersection == 'NORTH':
                next_item = item
                next_row = row - 1
                maze_array[row - 1][item] = 1
                
            elif next_intersection == 'SOUTH':
                next_item = item
                next_row = row + 1
                maze_array[row + 1][item] = 1
            
            elif next_intersection == 'WEST':
                next_item = item - 1
                next_row = row
                maze_array[row][item - 1] = 1
                
            elif next_intersection == 'EAST':
                next_item = item + 1
                next_row = row
                maze_array[row][item + 1] = 1

            # Add the randomly chosen unvisited neighbor to the visited list
            visited.append((next_row, next_item))

        # If there are no more unvisited neighbors, end the loop    
        else:
            break


'''Main Function'''

def generate_maze(maze_height, maze_width):
    '''Main maze generation function. Returns: 2D Numpy array with carved maze path, the start position, and the goal position'''

    # Create Maze array
    maze_array = generate_maze_array(maze_height, maze_width)

    # Set starting position (in form of (row, item)) and add it to visited list
    start_position = (1,1) 
    visited = [start_position] 
    
    # Generate maze
    visit(maze_array, visited, maze_height, maze_width)

    # Mark starting position with color
    maze_array[start_position[0]][start_position[1]] = 2  

    # Get the goal position and mark with color
    carved_spaces = ((row, item) for row in range(maze_height) for item in range(maze_width) if maze_array[row][item] == 1)
    goal_row, goal_item = max(carved_spaces) # Goal is the farthest position from start position
    maze_array[goal_row][goal_item] = 4
    
    return maze_array, start_position, (goal_row, goal_item)


if __name__ == "__main__":
    '''Main code to test'''

    maze_array, start, goal = generate_maze(5,5)

    # Display maze
    plt.imshow(maze_array, cmap='Greys', origin='upper')  
    plt.xticks([])
    plt.yticks([])
    plt.show()
    print(maze_array)