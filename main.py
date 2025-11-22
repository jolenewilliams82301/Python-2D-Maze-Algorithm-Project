'''
Jolene Williams
Capstone Project - Maze Algorithm Analysis
* 
'''
import numpy as np
import random as rn
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys
import timeit as ti
import seaborn as sns
import pandas as pd

'''File imports'''
from maze_generation import generate_maze
from A_star_algorithm import a_star_find_path
from DFS_algorithm import dfs_find_path
from data_collection import collect_node_visitations
from data_collection import collect_execution_times


def visualize_maze(maze_array, path, col, alg, title):
    '''Visualize the maze and the path of each algorithm's maze solution'''

    # Get the line representing the path
    path_row_vals = [row for (row, item) in path]
    path_item_vals = [item for (row, item) in path]

    # Display maze
    plt.figure(num=title)
    plt.imshow(maze_array, cmap='Greys', origin='upper')  

    # Plot the algorithm's path
    plt.plot( path_item_vals, path_row_vals, color = col, lw = 1, label=alg )

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
    
    # Data Analysis


    # Data for node visitations
    visitations_data = collect_node_visitations([len(astar_path), len(dfs_path)], ['A* Algorithm', 'DFS Algorithm'])
    (bar_x,bar_y) = visitations_data

    plt.figure(num='Node Visitations Per Algorithm')
    plt.bar(bar_x,bar_y)

    
    #plt.show()

    a = ti.repeat(lambda: a_star_find_path(maze_array,start,goal), repeat=5,number=60)
    d = ti.repeat(lambda: dfs_find_path(maze_array,start,goal), repeat=5,number=60)
    print(a)
    print(d)
