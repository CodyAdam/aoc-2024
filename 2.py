IN = open("in.txt", "r").read().splitlines()


def process1(nums):
    sign = 1
    for i in range(1,len(nums)):
        current = nums[i]
        prev = nums[i-1]

        if i == 1:
            if prev > current:
                sign = -1

        diff = current - prev
        if abs(diff) > 3 or abs(diff) < 1:
            return 0
        if sign != diff//abs(diff):
            return 0
        
    return 1

def process2(nums):
    for i in range(len(nums)):
        array_without_i = nums[:i] + nums[i+1:]
        if process1(array_without_i):
            return 1
    return 0

s1 = 0
s2 = 0 
for line in IN:
    nums = list(map(int, line.split()))
    s1 += process1(nums)
    s2 += process2(nums)

print(s1)
print(s2)
