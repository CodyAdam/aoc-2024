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
            if any(x == px and y == py for px, py in points):
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

def longest_chain(points_set: set):
    longest = 0
    current = 0
    for y in range(H):
        for x in range(W):
            if (x, y) in points_set:
                current +=1
                longest = max(longest, current)
            else: 
                current = 0
    return longest


def step(points, s):
    new_points = set()
    for p in points:
        new_points.add(new_pos(p, s))
    return new_points

W = 101
H = 103

new_points = step(points, 100)
s1 = prod(count(new_points))
print(s1)

for s in range(20000):
    new_points = step(points, s)
    if s % 1000 == 0:
        print("step:", s)
    if longest_chain(new_points) > 20:
        show(new_points)
        print("TREE FOUND chain:", longest_chain(new_points), "At:", s)
        break
else: 
    print("not found")
