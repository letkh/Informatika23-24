s = '>' + '1' * 15 + '4' * 16 + '6' * 20
while '>1' in s or '>4' in s or '>6' in s:
    if '>1' in s:
        s = s.replace('>1', '4161>', 1)
    if '>4' in s:
        s = s.replace('>4', '1611>', 1)
    if '>6' in s:
        s = s.replace('>6', '414>', 1)
print(sum(map(int, s[:-1])))