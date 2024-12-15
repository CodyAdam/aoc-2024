MAP, IN  = open("in.txt", "r").read().split("\n\n")

directions = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1),
}
grid = []
pos = (0,0)
for y, line in enumerate(MAP.splitlines()):
    grid.append([])
    for x, char in enumerate(line):
        if char == "@":
            pos = (x, y)
            grid[-1].append(".")
        else:
            grid[-1].append(char)
W = len(grid[0])
H = len(grid)

def show(grid, pos):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if ((x,y) == pos):
                print("@", end="")
            else: print(char, end="")
        print()
    print()


def move(grid, pos, dir):
    x, y = pos
    dx, dy = dir
    new_pos = (x + dx, y + dy)
    if is_box(grid, new_pos):
        if move_box_if_possible(grid, new_pos, dir):
            return grid, new_pos
        else:
            return grid, pos
    if is_out(grid, new_pos) or not is_free(grid, new_pos):
        return grid, pos
    return grid, new_pos

def is_out(grid, pos):
    x, y = pos
    return x < 0 or x >= W or y < 0 or y >= H

def is_box(grid, pos):
    x, y = pos
    return grid[y][x] == "O"

def is_free(grid, pos):
    x, y = pos
    return grid[y][x] == "."

def move_box_if_possible(grid, box_pos, direction):
    x, y = box_pos
    dx, dy = direction
    new_pos = (x + dx, y + dy)
    if is_free(grid, new_pos) or (is_box(grid, new_pos) and move_box_if_possible(grid, new_pos, direction)) :
        grid[y][x] = "."
        grid[y + dy][x + dx] = "O"
        return True
    return False

def score(grid):
    s = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "O":
                s += x + y * 100
    return s

show(grid, pos)
for char in IN:
    if char not in directions: continue
    direction = directions[char]
    grid, pos = move(grid, pos, direction)
    # print(char)
    # show(grid, pos)
s1 = score(grid)
print(s1)
