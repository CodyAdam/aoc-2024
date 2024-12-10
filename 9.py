
IN = open("in.txt", "r").read()
IN = list(map(int, list(IN)))


data = []  # (start index, count, label)
emptys = [] # (start index, count, label)
index = 0
for i, val in enumerate(IN):
    if i % 2 == 1:
        emptys.append((index, val, "."))
        index += val
    else:
        data.append((index, val, i//2))
        index += val

def show(data, emptys = []):
    data = filter(lambda x: x is not None, data)
    emptys = filter(lambda x: x is not None, emptys)
    both = list(data) + list(emptys)
    both.sort(key=lambda x: x[0])
    for start, count, char in both:
        for _ in range(start, start + count):
            print(char, end="")
    print()


def checksum(data, emptys):
    s = 0
    data = filter(lambda x: x is not None, data)
    emptys = filter(lambda x: x is not None, emptys)
    both = list(data) + list(emptys)
    both.sort(key=lambda x: x[0])
    index = -1
    for start, count, char in both:
        for _ in range(start, start + count):
            index += 1
            if (char == "."):
                continue
            s+= char * index
    return s

def trim(data, emptys):
    data = filter(lambda x: x[1] > 0, data)
    emptys = filter(lambda x: x[1] > 0, emptys)
    return data, emptys

def step_1(data, emptys):
    global changed
    changed = False
    if len(emptys) == 0:
        return data, emptys

    changed = True
    empty_index, empty_count, empty_label = emptys.pop(0)
    data_index, data_count, data_label = data.pop()
    to_remove = min(empty_count, data_count)

    data.append((empty_index, to_remove, data_label))
    if (empty_count - to_remove) > 0:
        emptys.append((empty_index + to_remove, empty_count - to_remove, empty_label))
    if (data_count - to_remove) > 0:
        data.append((data_index, data_count - to_remove, data_label))
    data = sorted(data, key=lambda x: x[0])
    emptys = sorted(emptys, key=lambda x: x[0])
    return data, emptys

def step_2(data, emptys):
    global changed
    changed = False
    if len(emptys) == 0:
        return data, emptys
    stop = False
    for i in range(len(data)-1, -1, -1):
        data_index, data_count, data_label = data[i]
        for j in range(len(emptys)):
            if stop:
                break
            empty_index, empty_count, empty_label = emptys[j]
            if data_index < empty_index or empty_count < data_count:
                continue
            # place data in empty
            data[i] = (empty_index, data_count, data_label)
            emptys.append((data_index, data_count, "."))
            if empty_count - data_count > 0:
                emptys[j] = (empty_index + data_count, empty_count - data_count, empty_label)
            else:
                emptys.pop(j)
            changed = True
            stop = True
    data = sorted(data, key=lambda x: x[0])
    emptys = sorted(emptys, key=lambda x: x[0])
    return data, emptys




# show(data, emptys)

changed = True
data1, emptys1 = data, emptys
while changed:
    data1, emptys1 = step_1(data1, emptys1)
    # show(data1, emptys1)

print(checksum(data1, emptys1))

changed = True
data2, emptys2 = data, emptys
while changed:
    data2, emptys2 = step_2(data2, emptys2)
    # show(data2, emptys2)

print(checksum(data2, emptys2))

