def is_near(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


c = 0
dig = '012345678'
for x1 in dig[1:]:
    for x2 in dig:
        for x3 in dig:
            for x4 in dig:
                for x5 in dig:
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count('5') == 1 and is_near(s):
                        c += 1
print(c)