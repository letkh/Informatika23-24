s = open('source/24-22.txt').readline()
mi = 0
c = 0
i = 0
while i < len(s)-2:
    if s[i] in "BCDFG" and s[i+1] in 'BCDFG' and s[i+2] in 'AE':
        mi = max(mi, c)
        c = 0
        i += 3
    else:
        c += 1
        i += 1
print(mi + 4)
