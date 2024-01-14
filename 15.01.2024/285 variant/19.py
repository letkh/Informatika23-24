def F(x, p):
    if x>=96 and p==3: return True
    if x<96 and p==3: return False
    if x>=96: return False
    
    if p%2==1:
        if x % 2 == 0:
            return F(x + 1, p + 1) and F(x + (x // 2), p + 1)
        elif x % 3 == 0:
            return F(x + 1, p + 1) and F(x + (x // 3), p + 1)
        elif x % 2 != 0 and x % 3 != 0:
            return F(x + 1, p + 1) and F(x * 2, p + 1)
    else:
        if x % 2 == 0:
            return F(x + 1, p + 1) or F(x + (x // 2), p + 1)
        elif x % 3 == 0:
            return F(x + 1, p + 1) or F(x + (x // 3), p + 1)
        elif x % 2 != 0 and x % 3 != 0:
            return F(x + 1, p + 1) or F(x * 2, p + 1)

for s in range(1, 95):
    if F(s, 1):
        print(s)