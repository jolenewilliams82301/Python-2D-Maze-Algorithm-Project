'''
Jolene Williams
Capstone Project - Maze Algorithm Analysis
* 
'''
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import pandas as pd
from time import perf_counter
import gc

'''File imports'''
from maze_generation import generate_maze
from A_star_algorithm import a_star_find_path
from DFS_algorithm import dfs_find_path
from BFS_algorithm import bfs_find_path

'''Helper Functions'''

def visualize_performance_data(df, ax):
    '''Visualize performance data'''

    node_visitations_bargraph = ax[1,0]
    execution_times_bargraph = ax[1,2]
    
    
    # Make labels bold for readability
    for label in node_visitations_bargraph.get_yticklabels():
        label.set_fontweight('bold')
    for label in execution_times_bargraph.get_xticklabels():
        label.set_fontweight('bold')

    # Bar graph for total node visitations per algorithm
    sns.barplot(ax=node_visitations_bargraph,y='algorithm_title', x='node_visitations', hue='algorithm_title', data=df, width=0.4)
    node_visitations_bargraph.set_ylabel("", fontsize=8)
    node_visitations_bargraph.set_xlabel("Node Visitations", fontsize=10, fontweight='bold')

    # Bar graph for execution time per algorithm
    sns.barplot(ax=execution_times_bargraph, x='algorithm_title', y= 'execution_time',hue='algorithm_title',data=df, width=0.4)
    execution_times_bargraph.set_xlabel("", fontsize=8)
    execution_times_bargraph.set_ylabel("Execution Time (seconds)", fontsize=10, fontweight='bold')
    

def visualize_all_mazes(maze_array, maze_paths, ax):
    '''Visualize all three mazes along with each algorithm's solution'''
    astar_path, dfs_path, bfs_path = maze_paths

    #fig1, (astar_ax, dfs_ax, bfs_ax) = plt.subplots(nrows=3,ncols=1)
    #fig1.suptitle('Mazes solved by each algorithm', fontweight='bold')
    astar_ax, dfs_ax, bfs_ax = ax[0,0], ax[0,1], ax[0,2]
    visualize_maze(maze_array, astar_path, 'red', 'A* Algorithm',  astar_ax)
    visualize_maze(maze_array, dfs_path, 'blue', 'DFS Algorithm',  dfs_ax)
    visualize_maze(maze_array, bfs_path, 'yellow', 'BFS Algorithm', bfs_ax)


def collect_data(algorithm_titles:list, path_lengths:list, execution_times:list):
    '''Collect data for data analysis/ visualization'''

    df = pd.DataFrame()

    df['execution_time'] = execution_times
    df['node_visitations'] = path_lengths
    df['algorithm_title'] = algorithm_titles

    return df


def visualize_maze(maze_array, path, color, alg, axes):
    '''Visualize the maze and the path of each algorithm's maze solution'''
    # Get the line representing the path
    path_row_vals = [row for (row, item) in path]
    path_item_vals = [item for (row, item) in path]

    # Display maze
    axes.imshow(maze_array, cmap='binary', origin='upper')

    # Plot the algorithm's path
    axes.plot(path_item_vals, path_row_vals, color=color, lw=1, label=alg)

    # other settings
    axes.set_xticks([])
    axes.set_yticks([])
    axes.legend()

'''Main Function'''

def maze_algorithm_analysis():
    '''Main function of the program. Generate a maze, solve using three algorithms, 
    show the mazes and each algorithm's solution, then visualize the performance data'''

    # Generate the maze
    maze_array, start, goal = generate_maze(20,40)
    maze_id = 0

    # Generate each algorithm's solution to the maze
    a_et_start = perf_counter()
    astar_path = a_star_find_path(maze_array, start, goal)
    a_et_end = perf_counter()

    dfs_et_start = perf_counter()
    dfs_path = dfs_find_path(maze_array, start, goal)
    dfs_et_end = perf_counter()

    bfs_et_start = perf_counter()
    bfs_path = bfs_find_path(maze_array, start, goal)
    bfs_et_end = perf_counter()

    # If the algorithm was not able to find a path
    if not astar_path:
        astar_path = [(0,0)]
    if not bfs_path:
        bfs_path = [(0,0)]
    if not dfs_path:
        dfs_path = [(0,0)]

    # Create figure to visualize the mazes and performance data
    fig, ax = plt.subplots(figsize=(15,10),nrows=2, ncols=3, height_ratios=[20,12])
    fig.suptitle('Mazes and Performance Data', fontweight='bold')
    ax[1,1].remove()

    # Visualize the maze along with each algorithm's solution
    maze_paths = (astar_path, dfs_path, bfs_path)
    visualize_all_mazes(maze_array, maze_paths, ax)
    
    # Record performance data in dataframe
    df = collect_data(['A*', 'DFS', 'BFS'],[len(astar_path), len(dfs_path), len(bfs_path)], 
                      [(a_et_end - a_et_start), (dfs_et_end - dfs_et_start), (bfs_et_end - bfs_et_start)])

    # Visualize the performance data in bar graphs
    visualize_performance_data(df, ax)
    # Display the data
    
    fig.tight_layout()
    #plt.show()
    plt.savefig('maze_algorithm_analysis.png',bbox_inches='tight', dpi=300)

    # Memory clean up
    plt.close(fig)

    gc.collect()
    
if __name__ == "__main__":
    maze_algorithm_analysis()