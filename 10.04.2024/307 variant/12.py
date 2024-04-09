for n in range(10000, 0, -1):
    s = '8' * n + '2'
    while '82' in s or '888' in s or '6666' in s:
        if '82' in s:
            s = s.replace('82', '28', 1)
        if '888' in s:
            s = s.replace('888', '62', 1)
        if '6666' in s:
            s = s.replace('6666', '6', 1)
        if s.count('6') == 8:
            print(n)