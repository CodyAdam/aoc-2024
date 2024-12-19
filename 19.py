from collections import defaultdict
OPTIONS, IN = open("in.txt", "r").read().split("\n\n")

OPTIONS = set(OPTIONS.split(", "))


def is_possible(line):
    global OPTIONS
    MAX = len(line)
    q = [0]
    while q:
        current = q.pop(0)
        if current == MAX:
            return True
        for i in range(1, MAX-current+1):
            if line[current:current+i] in OPTIONS and current+i not in q:
                q.append(current+i)
    return False

def find_possible_ways_dp(line):
    global OPTIONS
    cache = defaultdict(int)

    def dp(line):
        if len(line) == 0:
            return 1
        if len(line) == 1:
            return 1 if line in OPTIONS else 0
        if line in cache:
            return cache[line]
        for option in OPTIONS:
            if line.startswith(option):
                cache[line] += dp(line[len(option):])
        return cache[line]
    return dp(line)


s1 = 0
s2 = 0
for line in IN.splitlines():
    s1 += 1 if is_possible(line) else 0
    s2 += find_possible_ways_dp(line)
    print(line, s2)

print(s1)
print(s2)