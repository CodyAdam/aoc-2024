IN = open("in.txt", "r").read().splitlines()

WALLS = [(x,y) for x,y in [list(map(int, line.split(","))) for line in IN]]

END = (70, 70)
W = END[0]+1
H = END[1]+1

def is_oob(x,y):
    return x < 0 or x >= W or y < 0 or y >= H
def show(walls, visited):
    for y in range(H):
        for x in range(W):
            if (x,y) in walls:
                print("██", end="")
            elif (x,y) in visited:
                print("░░", end="")
            else:
                print(". ", end="")
        print()
    print()

def find_shortest_path(walls:list):
    walls = set(walls)
    pos = (0,0)
    end = END
    visited = set()
    visited.add(pos)
    queue = [(pos, 0)]
    # show(walls, visited)
    while queue:
        pos, dist = queue.pop(0)
        if pos == end:
            return dist
        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            new_pos = (pos[0]+d[0], pos[1]+d[1])
            if is_oob(new_pos[0], new_pos[1]) or new_pos in walls or new_pos in visited:
                continue
            visited.add(new_pos)
            queue.append((new_pos, dist+1))
    return None


s1 = find_shortest_path(WALLS[:12])

print("s1:",s1)

for i in range(len(WALLS)):
    walls = WALLS[:i]
    path = find_shortest_path(walls)
    if path is not None:
        print("     after",i)
    else:
        s2 = ",".join(map(str, WALLS[i-1]))
        break

print("s2:",s2)

