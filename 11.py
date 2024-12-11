IN = open("in.txt", "r").read()

nums = list(map(int, IN.split()))

print(nums)


cache = {}
hit_count = 0


def step(nums, count):
    global hit_count

    if len(nums) == 1:
        if count == 0:
            return 1
        val = nums[0]
        if (val, count) in cache:
            hit_count += 1
            return cache[(val, count)]
        
        res = 0
        if val == 0:
            res = step([1], count - 1)
        elif len(str(val)) % 2 == 0:
            left, right = str(val)[:len(str(val))//2], str(val)[len(str(val))//2:]
            left_val = int(left)
            right_val = int(right)
            res = step([left_val, right_val], count - 1)
        else: 
            res = step([val * 2024], count - 1)
        res = cache[(val, count)]
        return res
    else: # multiple, just split
        return sum([step([val], count) for val in nums])


s1 = step(nums, 25)
s2 = step(nums, 75)

print("cache hits", hit_count)
print(s1)
print(s2)

