def oct(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]

with open('source/17.txt') as f:
    s = [int(x) for x in f]
    count = 0
    max = 0
    for i in range(1, len(s)):
        if s[i] % 107 == 0:
            if s[i] > max:
                max = s[i]
    min = 1000000
    for i in range(1, len(s)-1):
        if s[i] > max or s[i+1] > max:
            if '36' in oct(s[i]) or '36' in oct(s[i+1]):
                count += 1
                if (s[i] + s[i+1] < min):
                    min = s[i] + s[i+1]
print(count, min)