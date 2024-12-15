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
            grid[-1].append(".")
            grid[-1].append(".")
            pos = (x * 2, y)
        if char == "#":
            grid[-1].append("#")
            grid[-1].append("#")
        if char == "O":
            grid[-1].append("[")
            grid[-1].append("]")
        if char == ".":
            grid[-1].append(".")
            grid[-1].append(".")
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
        if can_move_box(grid, new_pos, dir):
            print("CAN MOVE BOX")
            move_box(grid, new_pos, dir)
            return grid, new_pos
        else:
            return grid, pos
    if not is_free(grid, new_pos):
        return grid, pos
    return grid, new_pos

def is_box(grid, pos):
    x, y = pos
    return grid[y][x] == "[" or grid[y][x] == "]"

def is_free(grid, pos):
    x, y = pos
    return grid[y][x] == "."

def can_move_box(grid, box_pos, direction):
    x, y = box_pos
    dx, dy = direction
    cell = grid[y][x]
    if cell == "#":
        return False
    if cell == ".":
        return True
    if dy == 0:
        return can_move_box(grid, (x + dx, y), direction)
    else:
        left = (x, y) if cell == "[" else (x - 1, y)
        right = (x, y) if cell == "]" else (x + 1, y)
        new_left = (left[0] + dx, left[1] + dy)
        new_right = (right[0] + dx, right[1] + dy)  
        return can_move_box(grid, new_left, direction) and can_move_box(grid, new_right, direction)
    
    
def move_box(grid, box_pos, direction):
    x, y = box_pos
    dx, dy = direction
    cell = grid[y][x]
    if cell != "[" and cell != "]":
        return
    left = (x, y) if cell == "[" else (x - 1, y)
    right = (x + 1, y) if cell == "[" else (x, y)
    
    new_left = (left[0] + dx, left[1] + dy)
    new_right = (right[0] + dx, right[1] + dy)


    if (new_left != right):
        move_box(grid, new_left, direction)
    if (new_right != left):
        move_box(grid, new_right, direction)

    grid[left[1]][left[0]] = "."
    grid[right[1]][right[0]] = "."
    grid[new_left[1]][new_left[0]] = "[" 
    grid[new_right[1]][new_right[0]] = "]"
    
def score(grid):
    s = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "[":
                s += x + y * 100
    return s

show(grid, pos)
for char in IN:
    if char not in directions: continue
    direction = directions[char]
    # print(char)
    grid, pos = move(grid, pos, direction)
    # show(grid, pos)
s1 = score(grid)
show(grid, pos)
print(s1)
