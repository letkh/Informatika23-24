def F(x, y, p):
    if x + y >= 84 and p==4: return True
    if x + y < 84 and p==4: return False
    if x + y >= 84: return False

    if p%2==0:
        return F(x+1, y, p+1) and F(x+y*2, y, p+1) and F(x, y+1, p+1) and F(x, y+x*2, p+1)
    else:
        return F(x+1, y, p+1) or F(x+y*2, y, p+1) or F(x, y+1, p+1) or F(x, y+x*2, p+1)
  

for s in range(1, 75):
    if F(8, s, 1):
        print(s)