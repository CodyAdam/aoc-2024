IN = open("in.txt").read().splitlines()

MAP = []
pos = (0, 0)
for y, line in enumerate(IN):
    current_line = []
    for x, char in enumerate(line):
        if (char == "^"):
            pos = (x, y)
            char = "."
        current_line.append(char)
    MAP.append(current_line)
W = len(MAP[0])
H = len(MAP)
start = pos

def show(grid, seen, pos, indent = 0):
    seen = set([x for (x,_) in seen])
    for y in range(H):
        for _ in range(indent):
            print(" ", end="")
        for x in range(W):
            if (x, y) == pos:
                print("@", end=" ")
            elif (x, y) in seen:
                print("X", end=" ")
            else:
                print(grid[y][x], end=" ")
        print()
    print()

def rotate90(direction):
    x, y = direction
    return (-y, x)

def isOut(x, y):
    return x < 0 or x >= W or y < 0 or y >= H

def isLoop(grid, pos, direction):
    seen = set([(pos, direction)])
    i = 0
    while True:
        i += 1
        pos, direction = step(grid, pos, seen, direction)
        if pos is None:
            return False
        # show(grid, seen, pos, indent=4)
        if (pos, direction) in seen:
            return True
    

def step(grid, pos, seen, direction, check_loop=False):
    global s2
    x, y = pos
    dx, dy = direction
    next_x, next_y = x+dx, y+dy
    seen.add((pos, direction))

    if isOut(next_x, next_y):
        return (None, None)
    next_cell = grid[next_y][next_x]
    if next_cell == "#" or next_cell == "O":
        return step(grid, pos, seen, rotate90(direction), check_loop=check_loop)
    if check_loop and (next_x,next_x) != start:
        temp_grid = [x[:] for x in grid]
        temp_grid[next_y][next_x] = "O"
        if isLoop(temp_grid, start, (0, -1)):
            s2_options.add((next_x,next_y))
    return ((next_x, next_y), direction)

s2_options = set()
direction = (0, -1)
grid = MAP
seen = set([(pos, direction)])
while True:
    pos, direction = step(grid, pos, seen, direction, check_loop=True)
    if pos is None:
        break

s1 = len(set([x for (x,_) in seen]))
s2 = len(s2_options)
print(s1)
print(s2)
