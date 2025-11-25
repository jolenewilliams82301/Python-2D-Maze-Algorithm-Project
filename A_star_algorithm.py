'''
A* Algorithm Implementation

Notes:
x = row, y = item

'''
from maze_generation import generate_maze
import heapq

'''Helper Functions'''

def return_path(came_from, current_position):
    ''' Return path '''
    path = []

    while current_position in came_from:
        path.append(current_position)
        current_position = came_from[current_position]

    path.append(current_position)
    path = path[::-1]

    return path


def calc_heuristic(position, goal):
    ''' Calculate heuristic function (provides estimate of cost to reach goal from given node). 
    - Heuristic used: Manhattan Distance '''
    x1,y1 = position
    x2,y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def get_valid_neighbors(maze_array, position):
    ''' Get valid neighbors of position '''
    x,y = position
    rows, cols = maze_array.shape
    
    valid_values = {1,2,4}

    # All possible moves
    possible_moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

    return ( (nx, ny) for nx,ny in possible_moves 
            if 0<= nx <= rows and 0 <= ny <= cols and maze_array[nx][ny] in valid_values)

'''Main Function'''
def a_star_find_path(maze_array, start, goal):
    '''Main A* Function - returns path'''

    # Initialize open set, closed set and open_set_hash for more efficient checking
    # if neighbor is in the open set
    open_set = []
    open_set_hash = set()
    heapq.heappush(open_set, (0,start))
    open_set_hash.add(start)

    came_from = {}
    # Cost from start to the current node
    g_score = {start:0}
    # Estimates cost from start to goal through the current node
    f_score = {start: calc_heuristic(start, goal)}

    while open_set:

        current_f_score, current_position = heapq.heappop(open_set)

        # Ignore stale entries
        if current_f_score > f_score.get(current_position, float('inf')):
            continue

        # If the goal is reached, return path
        if current_position == goal:
            return return_path(came_from, current_position)
        
        for neighbor in get_valid_neighbors(maze_array, current_position):
            # Get temp g (cost from start to current node plus one)
            # distance between neighbor and current node should equal 1
            temp_g_score = g_score[current_position] + 1 

            if (neighbor not in g_score) or (temp_g_score < g_score[neighbor]):
                # if neighbor's g_score not recorded or temp g score is less than neighbor's g score
                # then add neighbor to came_from list, set its g_score to temp g score, and set its f score
                # to temp g score + heuristic(neighbor, goal)
                came_from[neighbor] = current_position
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + calc_heuristic(neighbor, goal)
                
                # Add neighbor to open set if it's not added already
                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_hash.add(neighbor)

    return None
    

if __name__ == "__main__":
    maze_array, start, goal = generate_maze(10,10)
    path = a_star_find_path(maze_array, start, goal)
    print(maze_array)
    print(path)