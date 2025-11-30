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
import tracemalloc
from time import perf_counter

'''Testing the execution time of the code and making changes accordingly'''
'''
cProfile.run("maze_algorithm_analysis()", 'analysis.prof')

with open("analysis_with_plt_show", "w") as f:
    stats = pstats.Stats("analysis.prof", stream=f)
    stats.sort_stats("tottime")
    stats.print_stats()
    '''
tracemalloc.start()
maze_algorithm_analysis()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print('Top 10 memory consuming lines')
for stat in top_stats[:10]:
    print(stat)
