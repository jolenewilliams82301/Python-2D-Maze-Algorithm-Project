'''
NCLab Capstone Project

Jolene Williams

main.py 
Starting point for the program

'''
from maze_algorithm_analysis import maze_algorithm_analysis


if __name__ == "__main__":
    print('-----------------------------------------------------------')
    print("Pathfinding Algorithm Analysis using 2D Mazes")
    print('-----------------------------------------------------------')
    print("Generating maze and performing algorithm analysis ...")
    id, filename = maze_algorithm_analysis()
    print(f"Generated Maze {id} and performed algorithm analysis. Results have been exported to file '{filename}'.")
