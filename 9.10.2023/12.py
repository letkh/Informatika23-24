s = '>' + '1' * 15 + '4' * 16 + '6' * 20

def sum(n):
    b = 0
    for a in n:
        if (a != '>'):
            b += int(a)
    return b

while ('>1' in s) or ('>4' in s) or ('>6' in s):
    if '>1' in s:
        s = s.replace('>1', '4161>')
    if '>4' in s:
        s = s.replace('>4', '1611>')
    if '>6' in s:
        s = s.replace('>6', '414>')

print(sum(s))