IN = open("in.txt").read().splitlines()
from itertools import permutations

DEBUG = False

def get_max_possible(current, remaining_nums, with_concat=False):
    # Try all multiplication
    mult_result = current * pow(max(remaining_nums), len(remaining_nums))
    # Try all addition
    add_result = current + sum(remaining_nums)
    # Try all concat
    concat_result = int(str(current) + "".join(map(str, remaining_nums))) if with_concat else 0

    return max(mult_result, add_result, concat_result)

def is_valid(total, operations, current_result=None, index=0, with_concat=False):
    # Initialize with first number
    if index == 0:
        return is_valid(total, operations, operations[0], 1, with_concat=with_concat)
    
    # If we've processed all numbers, check if we've reached our target
    if index == len(operations):
        return current_result == total
    
    if current_result > total:
        return False
     
    if get_max_possible(current_result, operations[index:], with_concat=with_concat) < total:  # If we can't possibly reach target
        return False
        
    # Try addition
    if is_valid(total, operations, current_result + operations[index], index + 1, with_concat=with_concat):
        return True
    
    # Try multiplication
    if is_valid(total, operations, current_result * operations[index], index + 1, with_concat=with_concat):
        return True
    
    # Try concat
    if with_concat and is_valid(total, operations, int(str(current_result) + str(operations[index])), index + 1, with_concat=True):
        return True
    
    return False

s1 = 0
s2 = 0
for line in IN:
    total, operations = line.split(":")
    total = int(total)
    operations = list(map(int, operations.split()))
    if is_valid(total, operations):
        s1 += total
    if is_valid(total, operations, with_concat=True):
        s2 += total


print(s1)
print(s2)