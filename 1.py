IN = open("in.txt", "r").read().splitlines()
from collections import Counter

left = []
right = []
s1 = 0
s2 = 0

for line in IN:
    a, b = map(int, line.split())
    left.append(a)
    right.append(b)

left.sort()
right.sort()
count= Counter(right)

for i in range(len(left)):
    s1 += abs(left[i] - right[i])
    s2 += left[i] * count[left[i]]

print("part1", s1)
print("part2", s2)