from collections import Counter

IN = open("in.txt", "r").read().splitlines()


def mix(a, s):
    return a ^ s

def prune(s):
    s %= 16777216
    return s

def next(s):
    s = prune(mix(s * 64, s)) # 64 in binary is 1000000
    s = prune(mix(s // 32, s)) # 32 in binary is 100000
    s = prune(mix(s * 2048, s)) # 2048 in binary is 1000000000000
    return s

s1 = 0
c = Counter()
MAX = 2000
for i in IN:
    val = int(i)
    change = []
    amounts = []
    # print(val, val% 10)
    for _ in range(MAX):
        current_digit = val % 10
        next_val = next(val)
        last_digit = next_val % 10
        change.append(last_digit - current_digit)
        amounts.append(last_digit)
        val = next_val
        # print(next_val, last_digit, last_digit - current_digit)
    
    visited = set()
    for i in range(4,MAX+1):
        if tuple(change[i-4:i]) in visited:
            continue
        four_last = change[i-4:i]
        amount = amounts[i-1]
        c[tuple(four_last)] += amount
        visited.add(tuple(four_last))

    s1 += val

s2 = max(c.values())

print(s1)
print(s2)
