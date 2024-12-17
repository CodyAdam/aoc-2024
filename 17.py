REG, PROG = open("in.txt", "r").read().split('\n\n')

r = {"A": 0, "B": 0, "C": 0}
prog = list(map(int, PROG.split(" ")[1].split(",")))
for line in REG.splitlines():
    letter = line.split(": ")[0].split(" ")[1]
    val = int(line.split(": ")[1])
    r[letter] = val

def run():
    A = r["A"]
    B = r["B"]
    C = r["C"]
    i = 0
    res = []
    seen = set()
    while i < len(prog):
        state_hash = (A, B, C, i)
        if state_hash in seen:
            print("Loop detected")
            return [] # Loop detected
        seen.add(state_hash)
        val = { 0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C }
        code = prog[i]
        op = prog[i+1]
        match code:
            case 0: A = A >> val[op]
            case 1: B = B ^ op
            case 2: B = val[op] % 8
            case 3: i = op-2 if A != 0 else i
            case 4: B = B ^ C
            case 5: res.append(val[op] % 8)
            case 6: B = A >> val[op]
            case 7: C = A >> val[op]
        i += 2
    return res

print(*run(), sep=",")

print("Target:", prog)
todo = [(0, 1)]
out = []
while todo:
    a, length = todo.pop(0)
    for i in range(8):
        r["A"] = a + i
        res = run()
        if (res == prog[-length:]):
            todo.append(((a + i) * 8 , length+1))
            print(a, res)
            if (length == len(prog)):
                out.append(a + i)
                print( "^ Good ^")
print("Found min:", min(out))
