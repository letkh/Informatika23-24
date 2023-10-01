with open('source/17-12.txt') as f:
    s = [int(x) for x in f]
    maxc = max(s)
    count = 0;
    b = 0;
    for i in range(1, len(s)):
        if (s[i] % 10 == 3):
            count += 1;
            b += s[i];
    b = b / count;
    count = 0;
    min = 10000;
    for i in range(1, len(s)-1):
        if (maxc % s[i] == 0 or maxc % s[i+1] == 0) and (s[i] + s[i+1] > b):
            count += 1
            if (s[i]+s[i+1] < min):
                min = s[i]+s[i+1]
                #print(s[i], s[i+1])

print(count, min)