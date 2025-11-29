from maze_algorithm_analysis import maze_algorithm_analysis
from maze_algorithm_analysis import visualize_maze
from maze_algorithm_analysis import visualize_all_mazes
import matplotlib.pyplot as plt
from maze_generation import generate_maze
from A_star_algorithm import a_star_find_path
from DFS_algorithm import dfs_find_path
from BFS_algorithm import bfs_find_path
import cProfile
import pstats
from time import perf_counter

'''Testing the execution time of the code and making changes accordingly'''

cProfile.run("maze_algorithm_analysis()", 'analysis.prof')

with open("analysis_with_plt_close_and_plt_savefig", "w") as f:
    stats = pstats.Stats("analysis.prof", stream=f)
    stats.sort_stats("tottime")
    stats.print_stats()