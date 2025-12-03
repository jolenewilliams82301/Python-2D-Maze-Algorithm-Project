'''
NCLab Capstone Project

Jolene Williams

main.py 
Starting point for the program

'''
from maze_algorithm_analysis import maze_algorithm_analysis


if __name__ == "__main__":
    print('-----------------------------------------------------------')
    print("Python Pathfinding Algorithm Analysis using 2D Mazes")
    print("NCLab Capstone Project 1 for Python Developer Course")
    print("Jolene Williams")
    print('-----------------------------------------------------------')
    print("Generating maze and algorithm performance data ...")
    id,garb_collect = maze_algorithm_analysis()
    print(f"Generated Maze {id} with algorithm performance data. Run program again to generate a new maze.")
