with open('17-11.txt') as f:
    s = [int(x) for x in f]
    res = []
    count = 0;
    max = 0;
    for i in range(1, len(s)-1):
        if abs(s[i]) % 10 == abs(s[i + 1]) % 10 and abs(s[i]) % 2 != 0:
            count += 1
            if (s[i]*s[i+1] > max):
                max = s[i]*s[i+1]
print(count, max)