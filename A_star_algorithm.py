'''
A* Algorithm Implementation

Notes:
x = row, y = item

'''
import math
import numpy as np
import random as rn
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys
from maze_generation import generate_maze

class Node():
    """Node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0


'''Helper Functions'''

def calc_heuristic(pos1, pos2):
    '''Calculate euclidean distance (heuristic) between pos1 and pos2'''
    x1,y1 = pos1
    x2,y2 = pos2
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))


def get_valid_neighbors(maze_array, position):
    '''Get valid neighbors of position (including diagonals)'''
    x,y = position
    rows, cols = maze_array.shape

    # All possible moves
    possible_moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

    return ( (nx, ny) for nx,ny in possible_moves if 0<= nx <= rows and 0 <= ny <= cols and (maze_array[nx,ny] == 1 or maze_array[nx,ny] == 4 or maze_array[nx,ny] == 2))


def get_path(goal_node:Node):
    '''Return path if the goal has been reached'''
    path = []
    current = goal_node

    while current is not None:
        path.append(current.position)
        current = current.parent
    
    return path[::-1] # Reversed to get path from start to goal


'''Main Function'''

def a_star_find_path(maze_array, start_position, goal_position):
    '''Main function for A* algorithm'''

    # Initialize nodes and open and closed lists
    start = Node(None, start_position)
    goal = Node(None, goal_position)
    open_list = [start]
    closed_list = []

    # Initialize node properties
    start.g = 0
    start.h = calc_heuristic(start.position, goal.position)
    start.f = start.g + start.h
    start.parent = None

    # Loop until open list is empty
    while len(open_list) != 0:

        # Set the current node as the node with the lowest f value
        current = min(open_list, key=lambda node: node.f)

        # Check if the goal has been reached, stop entire function and return the path
        if current.position == goal.position:
            return get_path(current)
        
        # Remove current from open_list, append to closed_list
        open_list.remove(current)
        closed_list.append(current)

        # Check all neighboring nodes
        for neighbor_position in get_valid_neighbors(maze_array, current.position):

            # Skip to next iteration if neighbor has already been explored
            if any(neighbor.position == neighbor_position for neighbor in closed_list):
                continue

            # Calculate new path cost (g value)
            new_g = current.g + 1  # All moves have equal cost of 1

            # Create new node for the neighbor
            neighbor = Node(current, neighbor_position)

            # If the neighbor is not in open_list, add it
            if neighbor not in open_list:
                open_list.append(neighbor)
            elif new_g >= neighbor.g:
                continue  # Skip this neighbor if a better path exists

            # Update node properties
            neighbor.g = new_g
            neighbor.h = calc_heuristic(neighbor.position, goal.position)
            neighbor.f = neighbor.g + neighbor.h

    # If we exit the loop without finding a path
    print("No path found.")
    return []  # Return empty list if no path is found

if __name__ == "__main__":
    maze_array, start, goal = generate_maze(5,5)

    print()

    print(maze_array)

    path = a_star_find_path(maze_array, start, goal)
    print(path)


