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


def visualize_maze(maze_array, path, col, alg, title):
    '''Visualize the maze and the path of each algorithm's maze solution'''

    # Get the line representing the path
    path_row_vals = [row for (row, item) in path]
    path_item_vals = [item for (row, item) in path]

    # Display maze
    plt.figure(num=title)
    plt.imshow(maze_array, cmap='Greys', origin='upper')  

    # Plot the algorithm's path
    plt.plot( path_item_vals, path_row_vals, color = col, lw = 3, label=alg )

    # other settings
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    
if __name__ == "__main__":

    # Generate the maze
    maze_array, start, goal = generate_maze(30,30)

    # Generate each algorithm's solution to the maze
    astar_path = a_star_find_path(maze_array, start, goal)
    dfs_path = dfs_find_path(maze_array, start, goal)

    # Visualize the maze along with each algorithm's solution
    visualize_maze(maze_array, astar_path, 'red', 'A* Algorithm', 'Maze Solved With A* Algorithm')
    visualize_maze(maze_array, dfs_path, 'blue', 'DFS Algorithm', 'Maze Solved With DFS Algorithm')
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