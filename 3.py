import re
IN = open("in.txt", "r").read()



regex1 = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
matches = regex1.findall(IN)
s1 = 0
for match in matches:
    a,b = map(int, match)
    s1 += a*b
print(s1)


regex2 = re.compile(r"(mul\(([0-9]{1,3}),([0-9]{1,3})\))|(do\(\))|(don't\(\))")
matches = regex2.findall(IN)
s2 = 0
product = 1
for match in matches:
    mul, a, b, do, dont = match
    if mul != "":
        a,b = map(int, [a,b])
        s2 += a*b*product
    elif do != "":
        product = 1
    elif dont != "":
        product = 0
print(s2)
