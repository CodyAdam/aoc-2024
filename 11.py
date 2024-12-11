import time
IN = open("in.txt", "r").read()

nums = list(map(int, IN.split()))

print(nums)

length_cache = {}

def step_length(val, count):
    if count == 0:
        return 1

    if (val, count) in length_cache:
        return length_cache[(val, count)]

    if val == 0:
        result = step_length(1, count - 1)
    elif len(str(val)) % 2 == 0:
        left, right = str(val)[:len(str(val))//2], str(val)[len(str(val))//2:]
        left_val = int(left)
        right_val = int(right)
        result = step_length(left_val, count - 1) + step_length(right_val, count - 1)
    else:
        result = step_length(val * 2024, count - 1)

    length_cache[(val, count)] = result
    return result

def total_length(nums, count):
    return sum(step_length(val, count) for val in nums)

s1 = total_length(nums, 25)
s2 = total_length(nums, 75)
print(s1)
print(s2)
