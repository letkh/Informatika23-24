def F(x, y, p):
    if x + y >= 255 and (p==3 or p==5): return True
    if x + y < 255 and p==5: return False
    if x + y >= 255: return False

    if p%2==1:
        return F(x+1, y, p+1) and F(x*2, y, p+1) and F(x, y+1, p+1) and  F(x, y*2, p+1)
    else:
         return F(x+1, y, p+1) or F(x*2, y, p+1) or F(x, y+1, p+1) or  F(x, y*2, p+1)


def F1(x, y, p):
    if x + y >= 255 and p==3: return True
    if x + y < 255 and p==3: return False
    if x + y >= 255: return False

    if p%2==1:
        return F1(x+1, y, p+1) and F1(x*2, y, p+1) and F1(x, y+1, p+1) and  F1(x, y*2, p+1)
    else:
         return F1(x+1, y, p+1) or F1(x*2, y, p+1) or F1(x, y+1, p+1) or  F1(x, y*2, p+1)

for s in range(1, 238):
    if F(s, 17, 1):
        print(s)

print()

for s in range(1, 238):
    if F1(s, 17, 1):
        print(s)