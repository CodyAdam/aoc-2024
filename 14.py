from math import prod
import sys
sys.setrecursionlimit(100000)

IN = open("in.txt", "r").read().splitlines()


points = []
for line in IN:
    # p=6,3 v=-1,-3
    pos, speed = line.split(" ")
    pos = pos.split("=")[1].split(",")
    speed = speed.split("=")[1].split(",")
    points.append((int(pos[0]), int(pos[1]), int(speed[0]), int(speed[1])))


def new_pos(point, step):
    global W, H
    x, y, vx, vy = point
    new_x = (x + vx * step) % W
    new_y = (y + vy * step) % H
    return new_x, new_y

def show(points):
    global W, H
    for y in range(H):
        for x in range(W):
            if any(x == px and y == py for px, py, _, _ in points):
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def count(points_set):
    global W, H
    # TOP LEFT QUADRANT
    tl = sum(1 for x, y in points_set if x < W // 2 and y < H // 2)
    # TOP RIGHT QUADRANT
    tr = sum(1 for x, y in points_set if x >= (W+1) // 2 and y < H // 2)
    # BOTTOM LEFT QUADRANT
    bl = sum(1 for x, y in points_set if x < W // 2 and y >= (H + 1) // 2)
    # BOTTOM RIGHT QUADRANT
    br = sum(1 for x, y in points_set if x >= (W + 1) // 2 and y >= (H + 1) // 2)
    return tl, tr, bl, br

def check_all_points_connected(points_set: set):
    visited = set()
    def dfs(x, y):
        if (x, y) in visited:
            return
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in visited:
                dfs(nx, ny)
    start = points_set.pop()
    dfs(start[0], start[1])
    print("percent", len(visited) / len(points_set))
    return len(visited) == len(points_set)

W = 101
H = 103

def step(points, s):
    new_points = set()
    for p in points:
        new_points.add(new_pos(p, s))
    return new_points

new_points = step(points, 100)
s1 = prod(count(new_points))
print(s1)

for s in range(1000):
    new_points = step(points, s)
    print(s)
    if check_all_points_connected(new_points):
        show(new_points)
        break
else: 
    print("not found")
