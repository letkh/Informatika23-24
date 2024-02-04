f = open('source/24-15.txt')
s = f.readline()
# s = s.replace('VWXYZ', '*')
c = 0
for i in range(len(s)-1):
    if s[i] in 'VWXYZ':
        if s[i-1] + s[i] in 'ZVWXYZ':
            k += 1
        else:
            k = 1
    else:
        k = 0
    c = max(c, k)
print(c)