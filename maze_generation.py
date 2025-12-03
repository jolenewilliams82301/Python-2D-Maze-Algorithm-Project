'''
Jolene Williams

Maze Generation

Notes:

In Numpy 2D array representing the maze, 0 is wall, 1 is a carved path

'''
import numpy as np
import random as rn
import matplotlib.pyplot as plt


def generate_goal_position(maze_array, maze_height, maze_width):
    '''Generate a suitably distant goal position for a maze after it has been randomly generated'''

    # Get the position in the carved path with the largest item (Y) value
    carved_spaces = ((row, item) for row in range(maze_height) for item in range(maze_width) if maze_array[row][item] == 1)
    pos_largest_item = max(carved_spaces, key=lambda t:t[1]) 

    # Get the position in the carved path with the largest row (X) value
    carved_spaces = ((row, item) for row in range(maze_height) for item in range(maze_width) if maze_array[row][item] == 1)
    pos_largest_row = max(carved_spaces, key=lambda t:t[0])

    # If the largest Y value is greater than the largest X value, set the goal as the position with the largest Y value
    # else, set the goal as the position with the largest X value
    goal_row, goal_item = pos_largest_item if pos_largest_item[1] > pos_largest_row[0] else pos_largest_row

    return (goal_row, goal_item)



def generate_maze_array(H,W):
    '''Generate maze array (2D numpy array) with H rows each with length W'''
    if (H >= 5) and (W >= 5):
        return np.zeros( (H,W), dtype=np.uint8)
    else:
        print("Height must be 5 or larger, Width must be 5 or larger")


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
            continue


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
    (goal_row, goal_item) = generate_goal_position(maze_array, maze_height, maze_width)
    maze_array[goal_row][goal_item] = 4
    
    return maze_array, start_position, (goal_row, goal_item)


if __name__ == "__main__":
    '''Main code to test'''

    maze_array, start, goal = generate_maze(7,7)

    # Display maze
    plt.imshow(maze_array, cmap='Blues', origin='upper')  
    plt.xticks([])
    plt.yticks([])
    plt.show()
    print(maze_array)
    