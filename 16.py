IN = open("in.txt").read().splitlines()

W = len(IN[0])
H = len(IN)
walls = set()
for y, row in enumerate(IN):
    for x, c in enumerate(row):
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)
        elif c == "#":
            walls.add((x, y))


def show(visited=set()):
    for y in range(H):
        for x in range(W):
            if (x, y) in walls:
                print("█████", end="")
            elif (x, y) in visited:
                print("  O  ", end="")
            elif (x, y) == start:
                print("  S  ", end="")
            elif (x, y) == end:
                print("  E  ", end="")
            else:
                if (x, y) in costs:
                    print(f"{costs[(x, y)]%100000:5}", end="")
                else:
                    print("  .  ", end="")
        print()

costs = {}

def bfs(start_x, start_y):
    global costs
    # Add direction to track turns (dx,dy)
    queue = [(start_x, start_y, 0, 1, 0)]  # Start going right
    costs[(start_x, start_y)] = 0
    
    while queue:
        x, y, cost, curr_dx, curr_dy = queue.pop(0)
        if (x, y) == end:
            continue
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in walls:
                new_cost = cost + 1
                # Check if turning 90 degrees
                if (dx, dy) != (curr_dx, curr_dy):
                    new_cost += 1000
                
                if (nx, ny) not in costs or costs[(nx, ny)] > new_cost:
                    costs[(nx, ny)] = new_cost
                    queue.append((nx, ny, new_cost, dx, dy))

bfs(*start)
show()  
print(costs[end])

def bfs2(start_x, start_y):
    global costs
    visited = set()
    queue = [(start_x, start_y, float("inf"))] # (x, y, prev_cost)
    while queue:
        x, y, prev_cost = queue.pop(0)
        if (x, y) == start or (x, y) in visited:
            continue
        visited.add((x, y))
        cost = costs[(x, y)]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in walls:
                new_cost = costs[(nx, ny)]
                if new_cost < cost:
                    queue.append((nx, ny, cost))
                if new_cost == prev_cost - 2:
                    queue.append((nx, ny, cost))
    return visited

visited = bfs2(*end)
show(visited)
print(len(visited) + 1)



