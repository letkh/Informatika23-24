with open('source/17-16.txt') as f:
    s = [int(x) for x in f]
    count = 0;
    min1 = 1111111111111;
    max1 = 0;
    for i in range(1, len(s)):
        if s[i] % 19 == 0 and s[i] > 0:
            min1 = min(min1, s[i])
    for i in range(1, len(s) - 1):
        if (s[i] + s[i+1]) < min1:
            count += 1
            max1 = max(max1, s[i] + s[i+1])
print(count, max1)