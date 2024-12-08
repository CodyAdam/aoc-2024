from collections import defaultdict

IN = open("in.txt", "r").read().splitlines()
grid = []
for line in IN:
    grid.append(list(line))
W, H = len(grid[0]), len(grid)

antenas = defaultdict(list)
anti = set()
anti_all = set()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != ".":
            antenas[cell].append((x, y))

def is_outside(x, y):
    return x < 0 or x >= W or y < 0 or y >= H

for letter, positions in antenas.items():
    for x, y in positions:
        for xx, yy in positions:
            if (x, y) == (xx, yy):
                continue
            new_x, new_y = x + (x - xx), y + (y - yy)
            anti_all.add((x, y))
            if not is_outside(new_x, new_y):
                anti.add((new_x, new_y))
            while not is_outside(new_x, new_y):
                anti_all.add((new_x, new_y))
                new_x += x - xx
                new_y += y - yy

def show(grid, anti):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) in anti:
                print("#", end="")
            else:
                print(cell, end="")
        print()


s1 = len(anti)        
s2 = len(anti_all)
print(s1)
print(s2)