def F(x, p):
    if x>=443 and p==3: return True
    if x<443 and p==3: return False
    if x>=443: return False

    if p%2==1:
        return F(x+1, p+1) and F(x+3, p+1) and F(x*2, p+1)
    else:
         return F(x+1, p+1) or F(x+3, p+1) or F(x*2, p+1)

for s in range(1, 443):
    if F(s, 1):
        print(s)