s = '>' + '1' * 32 + '4' * 11 + '6' * 22

def sum(n):
    b = 0
    for a in n:
        if (a != '>'):
            b += int(a)
    return b

while '>1' in s or '>4' in s or '>6' in s:
    if '>1' in s:
        s = s.replace('>1', '1661>', 1)
    if '>4' in s:
        s = s.replace('>4', '146141>', 1)
    if '>6' in s:
        s = s.replace('>6', '141>')

print(sum(s))