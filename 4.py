IN = open("in.txt", "r").read().splitlines()

W = len(IN[0])
H = len(IN)

def show(arr):
    for line in arr:
        for char in line:
            print(char, end=" ")
        print()
    print()

LR = [[char for char in row] for row in IN] # base


RL = [line[::-1] for line in LR]
# show(RL)

UD = [[LR[row][col] for row in range(H)] for col in range(W)]
# show(UD)

DU = [line[::-1] for line in UD]
# show(DU)

def get_diagonal(arr):
    out = []
    W = len(arr[0])
    H = len(arr)
    for diag_index in range(W+H-1):
        diagonal = []
        # Get starting row and col for this diagonal
        if diag_index < W:
            start_row = 0
            start_col = diag_index
        else:
            start_row = diag_index - W + 1
            start_col = W - 1
            
        row = start_row
        col = start_col
        
        # Follow diagonal down and left until we hit edge
        while row < H and col >= 0:
            diagonal.append(arr[row][col])
            row += 1
            col -= 1
            
        out.append(diagonal)
    return out


# DIAGONALS
DIAG_TR_BL = get_diagonal(LR)
DIAG_BL_TR = [line[::-1] for line in DIAG_TR_BL]

DIAG_TL_BR = get_diagonal(RL)
DIAG_BR_TL = [line[::-1] for line in DIAG_TL_BR]

import re

def count_xmas(arr): 
    regx = re.compile(r"XMAS")
    s = 0
    for line in arr:
        s += len(re.findall(regx, "".join(line)))
    return s

# show(LR)
print("Left to Right:", count_xmas(LR))
print("Right to Left:", count_xmas(RL))
print("Up to Down:", count_xmas(UD))
print("Down to Up:", count_xmas(DU))
print("Top Right to Bottom Left:", count_xmas(DIAG_TR_BL))
print("Bottom Left to Top Right:", count_xmas(DIAG_BL_TR))
print("Top Left to Bottom Right:", count_xmas(DIAG_TL_BR))
print("Bottom Right to Top Left:", count_xmas(DIAG_BR_TL))
print("Total:", count_xmas(LR) + count_xmas(RL) + count_xmas(UD) + count_xmas(DU) + 
      count_xmas(DIAG_TR_BL) + count_xmas(DIAG_BL_TR) + count_xmas(DIAG_TL_BR) + count_xmas(DIAG_BR_TL))


def check_xmas(arr, row, col):
    if row == 0 or col == 0 or row == H-1 or col == W-1:
        return False
    tl = arr[row-1][col-1]
    tr = arr[row-1][col+1]
    bl = arr[row+1][col-1]
    br = arr[row+1][col+1]
    
    up_down_xmas = tl == tr and bl == br and tl != bl and bl in ["S", "M"] and tl in ["S", "M"]
    left_right_xmas = tl == bl and tr == br and tl != tr and tl in ["S", "M"] and tr in ["S", "M"]
    
    return up_down_xmas or left_right_xmas

s2 = 0
for row in range(H):
    for col in range(W):
        letter = LR[row][col]
        if letter == "A" and check_xmas(LR, row, col):
            s2 +=1
print(s2)
