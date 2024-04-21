for n in range(4, 4000):
    s = '2' + '1' * n
    while '21' in s or '911' in s or '111' in s:
        if '21' in s:
            s = s.replace('21', '9', 1)
        if '911' in s:
            s = s.replace('911', '29', 1)
        if '111' in s:
            s = s.replace('111', '92', 1)
    if sum(map(int, s)) == 389:
        print(n)
        break