def F(x, y, p):
    if x + y >= 142 and p==3: return True
    if x + y < 142 and p==3: return False

    return F(x + 2, y, p+1) or F(x*2, y, p+1) or F(x, y + 2, p+1) or F(x, y*2, p+1)
  

for s in range(1, 138):
    if F(s, 2, 1):
        print(s)