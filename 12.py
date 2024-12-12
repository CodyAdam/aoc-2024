from collections import defaultdict

IN = open("in.txt", "r").read().splitlines()

grid = [list(line) for line in IN]
W = len(grid[0])
H = len(grid)


def get_neighbors(x, y):
    return  [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]



def is_outside(x, y):
    return x < 0 or x >= H or y < 0 or y >= W

def dfs_perimeter_area(x, y, cell, visited, local_visited = set()):
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    local_visited.add((x, y))
    s = 0
    for nx, ny in get_neighbors(x, y):
        if is_outside(nx, ny) or grid[nx][ny] != cell:
            s += 1
        elif grid[nx][ny] == cell:
            s += dfs_perimeter_area(nx, ny, cell, visited, local_visited)
    return s


def both_90_degrees_back(x, y):
    """Give [left rotation, right rotation, opposite]"""
    if (x, y) == (0, 1):
        return [(1, 0), (-1, 0), (0, -1)]
    elif (x, y) == (0, -1):
        return [(-1, 0), (1, 0), (0, 1)]
    elif (x, y) == (1, 0):
        return [(0, -1), (0, 1), (-1, 0)]
    elif (x, y) == (-1, 0):
        return [(0, 1), (0, -1), (1, 0)]

def check_side(x, y, direction, cell, side_visited):
    left, right, opposite = both_90_degrees_back(*direction)
    
    side_visited.add((x, y, direction))

    # Helper function to check one side
    def check_direction(start_x, start_y, move_x, move_y):
        curr_x, curr_y = start_x + move_x, start_y + move_y
        while True:
            # Check the cell on the opposite side
            opp_x = curr_x + opposite[0] 
            opp_y = curr_y + opposite[1]
        
            # Stop if opposite cell is outside or doesn't match target
            if is_outside(opp_x, opp_y) or grid[opp_y][opp_x] != cell:
                break
                
            # Stop if current cell is inside and matches target
            if not is_outside(curr_x, curr_y) and grid[curr_y][curr_x] == cell:
                break

            # Good, add to side_visited and count
            side_visited.add(((curr_x, curr_y), direction))
            curr_x += move_x
            curr_y += move_y
            
    check_direction(x, y, *left)
    check_direction(x, y, *right)

def dfs_side_area(x, y, cell, visited, local_visited = set(), side_visited = set()):
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    local_visited.add((x, y))
    s = 0
    for nx, ny in get_neighbors(x, y):
        direction = (nx-x, ny-y)
        if (is_outside(nx, ny) or grid[ny][nx] != cell) and ((nx, ny), direction) not in side_visited:
            check_side(nx, ny, direction, cell, side_visited)
            s += 1
        elif not is_outside(nx, ny) and grid[ny][nx] == cell:
            s += dfs_side_area(nx, ny, cell, visited, local_visited, side_visited)
    return s


s1 = 0
s2 = 0
visited_1 = set()
visited_2 = set()
side_visited = set()
for y in range(H):
    for x in range(W):
        cell = grid[y][x]
        local_visited_1 = set()
        local_visited_2 = set()
        s1 += dfs_perimeter_area(x, y, cell, visited_1, local_visited_1) * len(local_visited_1)
        s2 += dfs_side_area(x, y, cell, visited_2, local_visited_2) * len(local_visited_2)
print(s1)
print(s2)
