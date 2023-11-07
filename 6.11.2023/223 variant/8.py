def uniq(s):
    arr = []
    for x in range(9):
        arr.append(s[x])
    if len(set(arr)) == 9:
        return True
    else:
        return False
    
def isABC(s):
    c = True
    for x in range(3):
        if s[x] > s[x + 1]:
            c = False
    return c

k = 0
nabor = 'КОМПЬЮТЕР'
for x1 in nabor:
    for x2 in nabor:
        for x3 in nabor:
            for x4 in nabor:
                for x5 in nabor:
                    for x6 in nabor:
                        for x7 in nabor:
                            for x8 in nabor:
                                for x9 in nabor:
                                    s = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
                                    if uniq(s) and isABC(s) and s[8] == 'Е':
                                        k += 1
print(k)

