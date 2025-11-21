''''

Data Collection



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
import seaborn as sns
import pandas as pd

def func(input):
    return range(input)

def data_collection(visitation_totals:list, algorithm_titles:list):
    '''Collect data about each algorithm'''

    # Get visitations per algorithm data
    bar_x = algorithm_titles
    bar_y = visitation_totals

    bar_data = (bar_x, bar_y)

    return bar_data

if __name__ == "__main__":
    '''Main code to test'''

    (x,y) = data_collection([50,60,30], ['Alg', 'Alg2', 'Alg3'])

    
    plt.bar(x,y)
    plt.show()