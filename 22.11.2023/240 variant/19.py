def F(x, y, p):
    if x + y >= 255 and p==3: return True
    if x + y < 255 and p==3: return False

    return F(x+1, y, p+1) or F(x*2, y, p+1) or F(x, y+1, p+1) or F(x, y*2, p+1)
  

for s in range(1, 238):
    if F(s, 17, 1):
        print(s)