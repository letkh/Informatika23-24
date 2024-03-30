for n in range(4, 10000):
    s = '5' + '2' * n
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '22', 1)
        if '522' in s:
            s = s.replace('522', '25', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)

    if sum(map(int, s)) == 63:
        print(n)
        break