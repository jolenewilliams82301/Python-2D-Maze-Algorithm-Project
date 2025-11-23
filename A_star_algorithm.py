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

'''Helper Functions'''

def calc_heuristic(pos1, pos2):
    '''Calculate euclidean distance (heuristic) between pos1 and pos2'''
    x1,y1 = pos1
    x2,y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


def get_valid_neighbors(maze_array, position):
    '''Get valid neighbors of position'''
    x,y = position
    rows, cols = maze_array.shape

    # All possible moves
    possible_moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

    return ( (nx, ny) for nx,ny in possible_moves 
            if 0<= nx <= rows and 0 <= ny <= cols 
            and (maze_array[nx][ny] == 1 or maze_array[nx][ny] == 4 or maze_array[nx][ny] == 2))


def return_path(came_from:dict, current):
    '''Return path if the goal has been reached'''
    path = []

    while current in came_from:
        path.append(current)
        current = came_from[current]

    path.append(current)
    path = path[::-1]
    
    return path

if __name__ == "__main__":
    pass