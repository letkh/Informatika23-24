#12345
#ИПВПВ

def f(s, p):
    if s >= 136 and p == 4:
        return True
    if s < 136 and p == 4:
        return False
    if s >= 136:
        return False
    if p % 2 == 1:
        return f(s + 1, p + 1) or f(s * 4 - 3, p + 1)
    else:
        return f(s + 1, p + 1) and f(s * 4 - 3, p + 1)
for s in range(1, 135):
    if f(s, 1) == 1:
        print(s)