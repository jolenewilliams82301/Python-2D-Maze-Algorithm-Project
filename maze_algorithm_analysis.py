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


'''Helper Functions'''

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
    axes.set_xticks([])
    axes.set_yticks([])
    axes.legend()

'''Main Function'''

def maze_algorithm_analysis():
    '''Main function of the program. Generate a maze, solve using three algorithms, 
    show the mazes and each algorithm's solution, then visualize the performance data'''

    # Generate the maze
    maze_array, start, goal = generate_maze(20,50)
    maze_id = 0

    # Generate each algorithm's solution to the maze
    a_et_start = perf_counter()
    astar_path = a_star_find_path(maze_array, start, goal)
    a_et_end = perf_counter()

    dfs_et_start = perf_counter()
    dfs_path = dfs_find_path(maze_array, start, goal)
    dfs_et_end = perf_counter()
    
    '''Visualization'''

    # Visualize the maze along with each algorithm's solution
    fig1, (astar_ax, dfs_ax) = plt.subplots(nrows=2,ncols=1, figsize=(10,10))
    fig1.suptitle('Mazes solved by each algorithm')
    visualize_maze(maze_array, astar_path, 'red', 'A* Algorithm', 'A* Algorithm', astar_ax)
    visualize_maze(maze_array, dfs_path, 'blue', 'DFS Algorithm', 'DFS Algorithm', dfs_ax)
    fig1.tight_layout()

    # Get performance data in dataframe
    df = collect_data(['A* Algorithm', 'DFS Algorithm'],[len(astar_path), len(dfs_path)], [(a_et_end - a_et_start), (dfs_et_end - dfs_et_start)] )

    # Create bar graphs 
    fig2, (node_visitations_bargraph, execution_times_bargraph) = plt.subplots(nrows=2, ncols=1)
    fig2.suptitle('Performance Data', fontweight='bold')

    for label in node_visitations_bargraph.get_yticklabels():
        label.set_fontweight('bold')
    for label in execution_times_bargraph.get_yticklabels():
        label.set_fontweight('bold')
    for label in execution_times_bargraph.get_xticklabels():
        label.set_fontsize

    # Bar graph for total node visitations per algorithm
    sns.barplot(ax=node_visitations_bargraph,y='algorithm_title', x='node_visitations', hue='algorithm_title', data=df, width=0.4)
    node_visitations_bargraph.set_ylabel("", fontsize=10)
    node_visitations_bargraph.set_xlabel("Node Visitations", fontsize=10, fontweight='bold')

    # Bar graph for execution time per algorithm
    sns.barplot(ax=execution_times_bargraph, y='algorithm_title', x = 'execution_time',hue='algorithm_title',data=df, width=0.4)
    execution_times_bargraph.set_ylabel("", fontsize=10)
    execution_times_bargraph.set_xlabel("Execution Time (seconds)", fontsize=10, fontweight='bold')
    fig2.tight_layout()
    plt.show()

if __name__ == "__main__":
    maze_algorithm_analysis()