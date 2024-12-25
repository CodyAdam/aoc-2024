from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

IN = open("in.txt", "r").read().splitlines()

connections = defaultdict(set)

for i in IN:
    a, b = i.split("-")
    connections[a].add(b)
    connections[b].add(a)


def solve1():
    lans = set()
    for key,value in connections.items():
        for v1 in value:
            for v2 in value:
                if v1 != v2 and v2 in connections[v1]:
                    lans.add(tuple(sorted([v1, v2, key])))


    s1 = 0
    for l in lans:
        if len(l) == 3:
            for val in l:
                if val.startswith("t"):
                    s1 += 1
                    break

    print(s1)

def solve2():
    lans = set()
    for key, value in connections.items():
        connected = set([key])
        for v in value:
            all_connected = True
            for c in connected:
                if c not in connections[v]:
                    all_connected = False
            if all_connected:
                connected.add(v)
        lans.add(tuple(sorted(connected)))


    max_len = 0
    max_lan = None
    for l in lans:
        if len(l) > max_len:
            max_len = len(l)
            max_lan = l

    print(*max_lan, sep=",")

solve1()
solve2()