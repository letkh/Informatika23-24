def F(x, p):
    if x>=140 and (p==3 or p==5): return True
    if x<140 and p==5: return False
    if x>=140: return False

    if p%2==1:
        return F(x+1, p+1) and F(x+3, p+1) and F(x*4, p+1)
    else:
        return F(x+1, p+1) or F(x+3, p+1) or F(x*4, p+1)

def F1(x, p):
    if x>=140 and p==3: return True
    if x<140 and p==3: return False
    if x>=140: return False

    if p%2==1:
        return F1(x+1, p+1) and F1(x+3, p+1) and F1(x*4, p+1)
    else:
        return F1(x+1, p+1) or F1(x+3, p+1) or F1(x*4, p+1)

for s in range(1, 140):
    if F(s, 1):
        print(s)

print()

for s in range(1, 140):
    if F1(s, 1):
        print(s)