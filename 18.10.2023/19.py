def F(x, y, p):
    #print(f'x {x} y {y} sum: {x + y}, p: {p}')
    if x + y >= 84 and p==3: return True
    if x + y < 84 and p==3: return False
    return F(x+1, y, p+1) or F(x+y*2, y, p+1) or F(x, y+1, p+1) or F(x, y+x*2, p+1)

for s in range(1, 75):
    if F(8, s, 1):
        print(s)
        break