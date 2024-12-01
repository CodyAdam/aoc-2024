local file = io.open("in.txt", "r")

local left = {}
local right = {}
if file then
  IN = file:read("*a")
  file:close()

  for line in IN:gmatch("[^\r\n]+") do
    local a, b = line:match("^%s*(%S+)%s+(%S+)%s*$")
    if a and b then
      table.insert(left, a)
      table.insert(right, b)
    else
      print("Invalid line format:", line)
    end
  end
end


table.sort(left)
table.sort(right)
local s1 = 0
local s2 = 0

for i, v in ipairs(left) do
  local a = left[i]
  local b = right[i]
  s1 = s1 + math.abs(a - b)

  for j, w in ipairs(right) do
    if (w == a) then
      s2 = s2 + a
    end
  end
end

print("part1:", s1)
print("part2:", s2)