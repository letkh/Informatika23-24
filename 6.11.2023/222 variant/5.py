for n in range(10000000000000000, 100000000000000000):
    s = str(n)[::-1]
    sum = 0
    for j in range(len(s)):
        if j % 2 == 0:
            sum += int(s[j])
        else:
            b = 2 * int(s[j])
            if b > 9:
                q = b % 10 + b // 10
                sum = q
            else:
                sum += b
    if sum == 30:
        print(n)
        break