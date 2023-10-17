def F(x, y, p):
    if x + y >= 84 and (p==3 or p==5): return True
    if x + y < 84 and p==5: return False
    if x + y >= 84: return False

    if p%2==1:
        return F(x+1, y, p+1) and F(x+y*2, y, p+1) and F(x, y+1, p+1) and F(x, y+x*2, p+1)
    else:
        return F(x+1, y, p+1) or F(x+y*2, y, p+1) or F(x, y+1, p+1) or F(x, y+x*2, p+1)


def F1(x, y, p):
    if x + y >= 84 and p==3: return True
    if x + y < 84 and p==3: return False
    if x + y >= 84: return False

    if p%2==1:
        return F1(x+1, y, p+1) and F1(x+y*2, y, p+1) and F1(x, y+1, p+1) and F1(x, y+x*2, p+1)
    else:
        return F1(x+1, y, p+1) or F1(x*2, y, p+1) or F1(x, y+1, p+1) or  F1(x, y*2, p+1)

for s in range(1, 75):
    if F(8, s, 1):
        print(s)

print()

for s in range(1, 75):
    if F1(8, s, 1):
        print(s)