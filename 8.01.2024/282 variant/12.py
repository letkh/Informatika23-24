for n in range(4, 1000):
    s = '9' + '4'* n
    while '94' in s or '6444' in s or '444' in s:
        if '94' in s:
            s = s.replace('94','4',1)
        if '644' in s:
            s = s.replace('644','49',1)
        if '444' in s:
            s = s.replace('444', '6',1)
    if s.count('4') * 18 == n:
        print(n)