def F(x, y, p):
    if x + y >= 808 and (p==3 or p == 5): return True
    if x + y < 808 and p==5: return False
    if x + y >= 808: return False

    if p%2 == 1:
        return F(x + 2, y, p+1) and F(x*3, y, p+1) and F(x, y + 2, p+1) and F(x, y*3, p+1)
    else:
        return F(x + 2, y, p+1) or F(x*3, y, p+1) or F(x, y + 2, p+1) or F(x, y*3, p+1)

def F1(x, y, p):
    if x + y >= 808 and p==3: return True
    if x + y < 808 and p==3: return False
    if x + y >= 808: return False


for s in range(1, 300):
    if F(s, 35, 1):
        print(s)

print()

for s in range(1, 300):
    if F1(s, 35, 1):
        print(s)