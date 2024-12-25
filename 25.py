IN = open("in.txt", "r").read().split("\n\n")
W = 5
H = 7

locks = set()
keys = set()

for schema in IN:
    lines = schema.splitlines()
    current = []
    is_key = lines[0][0] == "."
    if is_key:
        for x in range(W):
            for y in range(H):
                if lines[y][x] == "#":
                    current.append(6-y)
                    break
        keys.add(tuple(current))
    else:
        for x in range(W):
            for y in range(H):
                if lines[y][x] == ".":
                    current.append(y-1)
                    break
        locks.add(tuple(current))


def match(key, lock):
    for i in range(len(key)):
        if not match_val(key[i], lock[i]):
            return False
    return True

def match_val(key_val, lock_val):
    return key_val + lock_val <= 5

print(keys, locks)

matching = set()
for key in keys:
    for lock in locks:
        if match(key, lock):
            matching.add((key, lock))

print(len(matching))
