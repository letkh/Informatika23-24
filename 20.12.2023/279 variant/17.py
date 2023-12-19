a = []
sum = 0
for i in range(1574, 9427):
    if i % 11 == 0 and i % 2 != 0 and i % 5 != 0 and i % 17 != 0 and i % 33 != 0:
        sum += i
        continue
    a.append(i)
length = 1
ml = 0
for i in range(len(a)-1):
    if a[i+1] - a[i] == 1:
        length += 1
        if ml < length:
            pos = [i-length, i]
            ml = max(length, ml)
    else:
        length = 1

print(sum, ml)