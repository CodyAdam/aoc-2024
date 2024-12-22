IN = open("in.txt").read().splitlines()

DIGIT_BUTTONS = {
    (0,0): "7",
    (1,0): "8",
    (2,0): "9",
    (0,1): "4",
    (1,1): "5",
    (2,1): "6",
    (0,2): "1",
    (1,2): "2",
    (2,2): "3",
    (1,3): "0",
    (2,3): "A",
}

DIGIT_BUTTONS_REVERSE = {v: k for k, v in DIGIT_BUTTONS.items()}

DIR_BUTTONS = {
    (1,0): "^",
    (2,0): "A",
    (0,1): "<",
    (1,1): "v",
    (2,1): ">",
}

DIR_BUTTONS_REVERSE = {v: k for k, v in DIR_BUTTONS.items()}

def get_best_option(a,b):
    ORDER = {
        "A": 0,
        "^": 1,
        ">": 2,
        "v": 3,
        "<": 4,
    }
    if len(a) != len(b):
        raise ValueError("Strings must be of the same length")
    if len(a) == 0:
        return ""
    char_a = a[0]
    char_b = b[0]
    if char_a == char_b:
        return char_a + get_best_option(a[1:], b[1:])
    else:
        val_a = ORDER[char_a]
        val_b = ORDER[char_b]
        if not val_a or not val_b:
            raise ValueError("Invalid character: " + char_a if not val_a else char_b)
        if val_a < val_b:
            return a
        else:
            return b

    



def gen_paths(buttons):
    paths = {}
    for b1 in buttons:
        for b2 in buttons:
            if b1 == b2:
                paths[(b1, b2)] = "A"
            
            diff_hor = b2[0] - b1[0]
            diff_ver = b2[1] - b1[1]
            horizontal = (">" * diff_hor if diff_hor > 0 else "<" * -diff_hor) 
            vertical = ("v" * diff_ver if diff_ver > 0 else "^" * -diff_ver)
            paths[(b1, b2)] = get_best_option(horizontal+vertical+"A", vertical+horizontal+"A")
    return paths

# for (start, end), path in sorted(gen_paths(DIR_BUTTONS).items()):
#     print(f"{DIR_BUTTONS[start]}   ->   {DIR_BUTTONS[end]}    {path}")

# for (start, end), path in sorted(gen_paths(DIGIT_BUTTONS).items()):
#     print(f"{DIGIT_BUTTONS[start]}   ->   {DIGIT_BUTTONS[end]}    {path}")

PATHS_DIGIT = gen_paths(DIGIT_BUTTONS)
PATHS_DIR = gen_paths(DIR_BUTTONS)
PATHS_DIR[((2,0), (0,2))] = "<v<A"

import re
s1 = 0
for line in IN:
    print(line)
    target = list(line)
    number_in_line = int("".join(re.compile(r"\d").findall(line)))
    for robot in range(26):
        if robot == 0:
            current_pos = DIGIT_BUTTONS_REVERSE["A"]
            path = ""
            while len(target):
                char = target.pop(0)
                target_pos = DIGIT_BUTTONS_REVERSE[char]
                path += PATHS_DIGIT[(current_pos, target_pos)]
                current_pos = target_pos
        else:
            current_pos = DIR_BUTTONS_REVERSE["A"]
            path = ""
            while len(target):
                char = target.pop(0)
                target_pos = DIR_BUTTONS_REVERSE[char]
                path += PATHS_DIR[(current_pos, target_pos)]
                current_pos = target_pos
        target = list(path)
    #     print(robot, path)
    # print(len(target), number_in_line)
    s1 += number_in_line * len(target)
print(s1)


# t = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
# for robot in range(26):
#     if robot == 0:
#         current_pos = DIGIT_BUTTONS_REVERSE["A"]
#         path = t
#         while len(path):
#             char = path.pop(0)
#             direction = DIGIT_BUTTONS_REVERSE[char]
#             print(char, target_pos)
#             current_pos = target_pos
#     else:
#         current_pos = DIR_BUTTONS_REVERSE["A"]
#         path = t
#         while len(path):
#             char = path.pop(0)
#             target_pos = DIR_BUTTONS_REVERSE[char]
#             print(char, target_pos)
#             current_pos = target_pos
#     t = path
#     print(path)
