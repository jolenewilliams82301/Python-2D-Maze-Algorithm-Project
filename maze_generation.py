"""
File: maze_generation.py
Author: Jolene Williams
Description: Randomly generate a 2D maze
NCLab Capstone Project 1
Notes:
-- In Numpy 2D array representing the maze, 0 is wall, 1 is a carved path

"""

import numpy as np
import random as rn
import matplotlib.pyplot as plt


def generate_goal_position(maze_array, maze_height, maze_width):
    ''' Generate the goal position for the randomly generated maze that is suitably far from the start position

        Keyword arguments:
        maze_array -- 2d numpy array representing the generated maze
        maze_height -- amount of rows in the maze array (height)
        maze_width -- the length of each row in the maze (width)
    '''
    # Get the position in the carved path with the largest item (Y) value
    carved_spaces = ((row, item) for row in range(maze_height) for item in range(maze_width) if maze_array[row][item] == 1)
    pos_largest_item = max(carved_spaces, key=lambda t:t[1]) 

    # Get the position in the carved path with the largest row (X) value
    carved_spaces = ((row, item) for row in range(maze_height) for item in range(maze_width) if maze_array[row][item] == 1)
    pos_largest_row = max(carved_spaces, key=lambda t:t[0])

    # If the largest Y value is greater than the largest X value, set the goal as the position with the largest Y value
    # Else, set the goal as the position with the largest X value
    goal_row, goal_item = pos_largest_item if pos_largest_item[1] > pos_largest_row[0] else pos_largest_row

    return (goal_row, goal_item)


def generate_maze_array(H,W):
    ''' Generate a numpy 2D array to represent the maze 

        Keyword arguments:
        H -- amount of rows in the maze array (height)
        W -- the length of each row in the maze (width)
    '''
    if (H >= 5) and (W >= 5):
        return np.zeros( (H,W), dtype=np.uint8)
    else:
        print("Height must be 5 or larger, Width must be 5 or larger")


def generate_unvisited_neighbors(row, item, maze_height, maze_width, visited):
    ''' Generate list of unvisited nodes adjacent to a given node (row, item)

        Keyword arguments:
        row -- row position of given node (x value)
        item -- item position of given node (y value)
        visited -- list of nodes that have been visited by the maze generation algorithm already
        maze_height -- amount of rows in the maze array (height)
        maze_width -- the length of each row in the maze (width)
    '''
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
    ''' Main function of the maze generation algorithm. For each node marked as visited,
        get a list of its unvisited neighbors. Randomly choose one of those neighbors,
        set it as carved path, mark it as visited, then repeat the process

        Keyword arguments:
        maze_array -- 2d numpy array representing the generated maze
        visited -- list of nodes that have been visited by the maze generation algorithm already
        maze_height -- amount of rows in the maze array (height)
        maze_width -- the length of each row in the maze (width)
    '''
    for (row, item) in visited:

        # Generate list of unvisited neighbors for each position marked as visited
        unvisited = generate_unvisited_neighbors(row, item, maze_height, maze_width, visited)

        if unvisited:
            
            # Randomly choose an unvisited neighbor and carve an empty space
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
            continue


def generate_maze(maze_height, maze_width):
    ''' Main maze generation function. Generates a numpy 2D array representing the maze, carves
        out the path with the maze generation algorithm, then generates the goal position. 

        Keyword arguments:
        maze_height -- amount of rows in the maze array (height)
        maze_width -- the length of each row in the maze (width)
    '''
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
    (goal_row, goal_item) = generate_goal_position(maze_array, maze_height, maze_width)
    maze_array[goal_row][goal_item] = 4
    
    return maze_array, start_position, (goal_row, goal_item)


if __name__ == "__main__":
    # For testing
    maze_array, start, goal = generate_maze(7,7)

    # Display maze
    plt.imshow(maze_array, cmap='Blues', origin='upper')  
    plt.xticks([])
    plt.yticks([])
    plt.show()
    print(maze_array)
    