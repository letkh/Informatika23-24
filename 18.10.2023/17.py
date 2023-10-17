with open('source/17-14.txt') as f:
    s = [int(x) for x in f]
    count = 0;
    max = 0;
    for i in range(1, len(s)):
        if str(abs(s[i])).count('4') >= 1:
            count += 1
            print(s[i])
            if (s[i] > max):
                max = s[i]
print(count, max)