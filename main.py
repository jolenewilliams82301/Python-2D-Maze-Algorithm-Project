'''
Jolene Williams
Capstone Project - Maze Algorithm Analysis
* 



'''
import math
import numpy as np
import random as rn
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys
from maze_generation import generate_maze
from A_star_algorithm import a_star_find_path
from DFS_algorithm import dfs_find_path


if __name__ == "__main__":

    maze_array, start, goal = generate_maze(5,5)

    plt.imshow(maze_array, cmap='Greys', origin='upper')  
    plt.xticks([])
    plt.yticks([])
    plt.show()
    print(maze_array)

    print(f'A* Algorithm : {a_star_find_path(maze_array, start, goal)}')
    print(f'DFS Algorithm : {dfs_find_path(maze_array, start, goal)}')
