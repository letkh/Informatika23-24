def F(x, p):
    if x>=84 and p==3: return True
    if x<84 and p==3: return False
    if x>=84: return False

    if p%2==1:
        if x % 2 == 0:
            return F(x+1, p+1) and F(x*1.5, p+1)
        else:
            return F(x+1, p+1) and F(x*2, p+1)
    else:
        if x % 2 == 0:
            return F(x+1, p+1) or F(x*1.5, p+1)
        else:
            return F(x+1, p+1) or F(x*2, p+1)

for s in range(1, 83):
    if F(s, 1):
        print(s)