def F(x, p):
    if x>=122 and p==3: return True
    if x<122 and p==3: return False
    if x>=122: return False

    if p%2==1:
        return F(x+1, p+1) and F(x+3, p+1) and F(x*5, p+1)
    else:
         return F(x+1, p+1) or F(x+3, p+1) or F(x*5, p+1)
for s in range(1, 29):
    if F(s, 1):
        print(s)