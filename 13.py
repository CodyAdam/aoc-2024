IN = open("in.txt", 'r').read().split("\n\n")

COST_A = 3
COST_B = 1

def get_games(offset = 0):
    games = []
    for game in IN:
        a, b, prize = game.splitlines()
        
        # Extract button A coordinates
        ax = int(a.split("X+")[1].split(",")[0])
        ay = int(a.split("Y+")[1])
        
        # Extract button B coordinates
        bx = int(b.split("X+")[1].split(",")[0])
        by = int(b.split("Y+")[1])
        
        # Extract prize coordinates
        px = int(prize.split("X=")[1].split(",")[0])
        py = int(prize.split("Y=")[1])
        
        button_a = (ax, ay)
        button_b = (bx, by)
        prize = (px + offset, py + offset)
        games.append((button_a, button_b, prize))
    return games

def solve_linear_combination(target, a, b):
    tx, ty = target
    ax, ay = a
    bx, by = b
    
    det = ax * by - ay * bx
    if det == 0:
        return None
    
    # calc coefficients using Cramer's rule
    a = (tx * by - ty * bx) / det
    b = (ax * ty - ay * tx) / det
    
    if a != int(a) or b != int(b):
        return None
    
    a = int(a)
    b = int(b)
    
    if a < 0 or b < 0:
        return None
        
    return (a, b)

s1 = 0
for button_a, button_b, prize in get_games():
    result = solve_linear_combination(prize, button_a, button_b)
    if result:
        a, b = result
        s1 += COST_A * a + COST_B * b
s2 = 0
for button_a, button_b, prize in get_games(10000000000000):
    result = solve_linear_combination(prize, button_a, button_b)
    if result:
        a, b = result
        s2 += COST_A * a + COST_B * b

print(s1)
print(s2)

