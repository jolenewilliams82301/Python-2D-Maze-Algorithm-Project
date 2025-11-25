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
from time import perf_counter

'''File imports'''
from maze_generation import generate_maze
from A_star_algorithm import a_star_find_path
from DFS_algorithm import dfs_find_path


def collect_data(algorithm_titles:list, path_lengths:list, execution_times:list):
    '''Collect data for data analysis/ visualization'''

    df = pd.DataFrame()
    df['execution_time'] = execution_times
    df['node_visitations'] = path_lengths
    df['algorithm_title'] = algorithm_titles

    return df


def visualize_maze(maze_array, path, col, alg, title, axes):
    '''Visualize the maze and the path of each algorithm's maze solution'''

    # Get the line representing the path
    path_row_vals = [row for (row, item) in path]
    path_item_vals = [item for (row, item) in path]

    # Display maze
    axes.imshow(maze_array, cmap='Greys', origin='upper')  

    # Plot the algorithm's path
    axes.plot( path_item_vals, path_row_vals, color = col, lw = 1, label=alg )

    # other settings
    axes.legend()
    axes.minorticks_off()
    
def maze_algorithm_analysis():

    # Generate the maze
    maze_array, start, goal = generate_maze(20,50)

    # Generate each algorithm's solution to the maze
    a_et_start = perf_counter()
    astar_path = a_star_find_path(maze_array, start, goal)
    a_et_end = perf_counter()

    dfs_et_start = perf_counter()
    dfs_path = dfs_find_path(maze_array, start, goal)
    dfs_et_end = perf_counter()
    
    # Visualize the maze along with each algorithm's solution
    fig1, (astar_ax, dfs_ax) = plt.subplots(nrows=2,ncols=1, figsize=(10,10))
    fig1.suptitle('Mazes solved by each algorithm')
    visualize_maze(maze_array, astar_path, 'red', 'A* Algorithm', 'A* Algorithm', astar_ax)
    visualize_maze(maze_array, dfs_path, 'blue', 'DFS Algorithm', 'DFS Algorithm', dfs_ax)
    
    # Data Analysis


    # Data for node visitations
    df = collect_data(['A* Algorithm', 'DFS Algorithm'],[len(astar_path), len(dfs_path)], [(a_et_end - a_et_start), (dfs_et_end - dfs_et_start)] )


    fig2, (bargraph1, bargraph2) = plt.subplots(nrows=2, ncols=1)
    sns.set_theme(color_codes=True)
    sns.barplot(ax=bargraph1,x='algorithm_title', y='node_visitations', data=df)
    sns.barplot(ax=bargraph2, x='algorithm_title', y = 'execution_time',data=df)
    plt.show()

if __name__ == "__main__":
    maze_algorithm_analysis()