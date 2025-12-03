"""
File: DFS_algorithm.py
Author: Jolene Williams
Description: BFS Algorithm implementation
NCLab Capstone Project 1

"""

from maze_generation import generate_maze
from collections import deque


def bfs_find_path(maze_array, start, goal):
    ''' Main BFS function. Solve maze with BFS and 
        return solution path

        Keyword arguments:
        maze_array -- 2d numpy array representing maze
        start -- the start position
        goal -- the goal position
    '''
    # Create a queue and add the start position
    queue = deque([start])  

    # Keep track of paths
    paths = {start: None}   
    
    height, width = maze_array.shape

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:

        current = queue.popleft()

        # If the goal has been reached, end loop
        if current == goal:
            break

        for direction in directions:
            nx, ny = current[0] + direction[0], current[1] + direction[1]
            if 0 <= nx < height and 0 <= ny < width and maze_array[nx][ny] in {1,2,4} and (nx, ny) not in paths:
                queue.append((nx, ny))
                paths[(nx, ny)] = current  # Track the path

    # Reconstruct the path from end to start
    path = []
    while goal is not None:
        path.insert(0, goal)
        goal = paths[goal]
    return path


if __name__ == "__main__":
    # For testing

    maze_array, start, goal = generate_maze(5,17)
    path = bfs_find_path(maze_array, start, goal)
    print(maze_array)
    print(path)
