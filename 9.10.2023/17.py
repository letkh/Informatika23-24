with open('source/17.txt') as f:
    s = [int(x) for x in f]
    count = 0;
    min = 10000;
    for i in range(1, len(s)):
        if str(abs(s[i])).count('6') > 0:
            count += 1
            print(s[i])
            if (s[i] < min):
                min = s[i]
print(count, min)