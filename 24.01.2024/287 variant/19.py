#12345
#ИПВПВ

def f(s, p):
    if s >= 136 and p == 3:
        return True
    if s < 136 and p == 3:
        return False
    if s >= 136:
        return False

    return f(s + 1, p + 1) or f(s * 4 - 3, p + 1)

for s in range(1, 135):
    if f(s, 1) == 1:
        print(s)