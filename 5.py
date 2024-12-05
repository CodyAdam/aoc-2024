from collections import defaultdict
RULES, IN = open("in.txt", "r").read().split("\n\n")
lines = IN.split("\n")


rules = defaultdict(list)
inv_rules = defaultdict(list)

for r in RULES.split("\n"):
    a,b = r.split("|")
    a = int(a)
    b = int(b)
    rules[a].append(b)
    inv_rules[b].append(a)


def is_correct(nums):
    global rules
    seen = set()
    for i,val in enumerate(nums):
        if (val in rules):
            for r in rules[val]:
                if (r in seen):
                    return False
        seen.add(val)
    return True

def fix(nums):
    global inv_rules
    i = 0
    while i < len(nums):
        val = nums[i]
        right = set(nums[i+1:])
        if (val in inv_rules):
            for r in inv_rules[val]:
                if (r in right):
                    # move val to the end of the list
                    nums.remove(val)
                    nums.append(val)   
                    i -= 1               
                    break
        i += 1
    return nums

s1 = 0
s2 = 0
for line in lines:
    nums = list(map(int, line.split(",")))
    if (is_correct(nums)):
        middle = nums[len(nums)//2]
        s1 += middle
    else:
        fixed = fix(nums)
        middle = fixed[len(fixed)//2]
        s2 += middle
    
        
print(s1)
print(s2)