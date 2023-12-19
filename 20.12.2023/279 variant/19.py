def F(x, p):
    if x>=26 and p==3: return True
    if x<26 and p==3: return False
    if x>=26: return False
    
    return F(x+1, p+1) or F(x+3, p+1) or F(x*2, p+1)

for s in range(1, 25):
    if F(s, 1):
        print(s)