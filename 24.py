from functools import cache

VARS, OPS = open("in.txt", "r").read().split("\n\n")

values = {}
for var in VARS.splitlines():
    name, val = var.split(": ")
    values[name] = int(val)


operations = {} # result -> (left, op, right)

for op in OPS.splitlines():
    exp, result = op.split(" -> ")
    left, op, right = exp.split(" ")
    operations[result] = (left, op, right)



def eval(name):
    global values, operations
    if name in values:
        return values[name]
    if name not in operations:
        raise Exception(f"Unknown variable: {name}")
    left, op, right = operations[name]
    left_val = eval(left)
    right_val = eval(right)
    if op == "AND":
        return left_val & right_val
    elif op == "OR":
        return left_val | right_val
    elif op == "XOR":
        return left_val ^ right_val
    raise Exception(f"Unknown operation: {op}")


z_keys = []
for key in operations:
    if key.startswith("z"):
        z_keys.append(key)

z_keys.sort()

print(len(set(operations.keys())) ** 4)

binary = []
for key in z_keys:
    binary.append(str(eval(key)))

binary.reverse()
print(int("".join(binary), 2))
