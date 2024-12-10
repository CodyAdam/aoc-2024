IN = open("in.txt", "r").read().splitlines()

grid = []
starts = set()
for y, line in enumerate(IN):
    for x, c in enumerate(line):
        if c == "0": 
            starts.add((x, y))
    grid.append(list(map(int, line)))


def get_neighbours(x, y):
    neighbours = []
    if x > 0:
        neighbours.append((x-1, y))
    if x < len(grid[0]) - 1:
        neighbours.append((x+1, y))
    if y > 0:
        neighbours.append((x, y-1))
    if y < len(grid) - 1:
        neighbours.append((x, y+1))
    return neighbours
    

def dfs_1(x, y, visited):
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    if grid[y][x] == 9:
        return 1
    s = 0
    for nx, ny in get_neighbours(x, y):
        if grid[y][x] == grid[ny][nx] - 1:
            s += dfs_1(nx, ny, visited)
    return s

def dfs_2(x, y, visited):
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    if grid[y][x] == 9:
        return 1
    s = 0
    for nx, ny in get_neighbours(x, y):
        if grid[y][x] == grid[ny][nx] - 1:
            s += dfs_2(nx, ny, set(visited)) # only diff is passing a copy of visited
    return s


s1 = 0
s2 = 0 
for x,y in starts:
    s1 += dfs_1(x, y, set())
    s2 += dfs_2(x, y, set())

print(s1)
print(s2)
