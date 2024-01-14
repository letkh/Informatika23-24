f = open('source/17-29.txt')
a = [int(s) for s in f]
max123 = max(x for x in a if x % 1000 == 123)
sum_troyki = []
for i in range(len(a)-2):
    if ((len(str(a[i])) == 5) + (len(str(a[i+1])) == 5) + (len(str(a[i+2])) == 5)) >= 2 and ((a[i] % 3 == 0) + (a[i+1] % 3 == 0) + (a[i+2] % 3 == 0)) and ((a[i]+a[i+1]+a[i+2]) > max123):
        sum_troyki.append(a[i] + a[i+1] + a[i+2])
print(len(sum_troyki), max(sum_troyki))