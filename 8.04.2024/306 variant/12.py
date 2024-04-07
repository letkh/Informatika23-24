for n in range(4, 10000):
    s = '9' + '1' * n
    while '91' in s or '111' in s or '99999' in s:
        if '91' in s:
            s = s.replace('91', '99', 1)
        if '111' in s:
            s = s.replace('111', '22', 1)
        if '99999' in s:
            s = s.replace('99999', '11', 1)
    if sum(map(int, s)) <= 123:
        print(n)