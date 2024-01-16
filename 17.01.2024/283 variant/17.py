f = open('source/17-29.txt')
a = [int(s) for s in f]
sum1 = []
for i in range(0, len(a)-3):
    if ((abs(a[i]) % 100 == 13) ^ (abs(a[i+3]) % 100 == 13)):
        sum1.append(a[i] + a[i+3])
print(len(sum1), max(sum1))