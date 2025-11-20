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
import timeit as ti

if __name__ == "__main__":

    # Generate the maze
    maze_array, start, goal = generate_maze(20,20)

    # Display the maze
   
    astar_path = a_star_find_path(maze_array, start, goal)
    dfs_path = dfs_find_path(maze_array, start, goal)

    # Testing plotting
    astar_path = astar_path
    astar_y_vals = [x for (x,y) in astar_path]
    astar_x_vals = [y for (x,y) in astar_path]

    plt.imshow(maze_array, cmap='Greys', origin='upper')  
    plt.xticks([])
    plt.yticks([])

    
    plt.plot(astar_x_vals, astar_y_vals, )
    plt.show()
    print(maze_array)

    '''
    print(f'DFS Algorithm : {dfs_find_path(maze_array, start, goal)}')
    dfs_time = ti.repeat(lambda: dfs_find_path(maze_array,start,goal), repeat=5, number=1000)
    print(dfs_time)

    print(f'A* Algorithm: {a_star_find_path(maze_array, start, goal)}')
    astar_time = ti.repeat(lambda: a_star_find_path(maze_array, start, goal), repeat=5, number=1000)
    print(astar_time)
    '''