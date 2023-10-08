with open('17.txt') as f:
    s = [int(x) for x in f]
    maxc = max(s)
    count = 0;
    b = 0;
    max = 0;
    for i in range(1, len(s)-3):
        if ((s[i] % 10 == 0 and s[i+1] % 10 != 0 and s[i+2] % 10 != 0) or (s[i] % 10 != 0 and s[i+1] % 10 == 0 and s[i+2] % 10 != 0) or (s[i] % 10 != 0 and s[i+1] % 10 != 0 and s[i+2] % 10 == 0)) and (s[i] + s[i+1] + s[i+2] < maxc):
            count += 1
            print(s[i], s[i+1], s[i+2])
            if (s[i] + s[i+1] + s[i+2] > max):
                max = s[i]+s[i+1]+s[i+2]
                #print(s[i], s[i+1])

print(count, max)