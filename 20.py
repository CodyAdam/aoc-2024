from collections import Counter

IN = open("in.txt").read().splitlines()

W = len(IN[0])
H = len(IN)
walls = set()
for y, line in enumerate(IN):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)
        elif c == "#":
            walls.add((x, y))


dist = {} # (x, y) -> dist from end 

def show(visited=set()):
    for y in range(H):
        for x in range(W):
            if (x, y) in walls:
                print("███", end="")
            elif (x, y) in visited:
                print(" O ", end="")
            elif (x, y) == start:
                print(" S ", end="")
            elif (x, y) == end:
                print(" E ", end="")
            else:
                if (x, y) in dist:
                    print(f"{dist[(x, y)]%100000:3}", end="")
                else:
                    print(" . ", end="")
        print()

def bfs(start):
    q = [start]
    dist[start] = 0
    while q:
        x, y = q.pop(0)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H:
                if (nx, ny) in walls:
                    continue
                if (nx, ny) in dist:
                    continue
                dist[(nx, ny)] = dist[(x, y)] + 1
                q.append((nx, ny))

def jump_options(jump_dist=2):
    options = []
    for nx in range(-jump_dist, jump_dist+1):
        for ny in range(-jump_dist, jump_dist+1):
            if abs(nx) + abs(ny) == jump_dist:
                options.append((nx, ny, jump_dist))
    return options

def second_pass_with_jumps(options):
    counter = Counter()
    for x, y in dist:
        for dx, dy, jump_dist in options:
            end_pos = (x + dx, y + dy)
            if end_pos in dist:
                diff = dist[end_pos] - dist[(x,y)] - jump_dist
                if diff > 0:
                    counter[diff] += 1
    return counter

def count_jumps_with_diff_over_100(counter):
    return sum(val for c, val in sorted(counter.items()) if c >= 100)

bfs(start) # precompute distances
show()


options_s1 = jump_options(2)
counter_s1 = second_pass_with_jumps(options_s1)
print(count_jumps_with_diff_over_100(counter_s1))


options_s2 = [opt for dist in range(1, 21) for opt in jump_options(dist)]
counter_s2 = second_pass_with_jumps(options_s2)
print(count_jumps_with_diff_over_100(counter_s2))
