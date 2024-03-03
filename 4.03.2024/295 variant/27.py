f = open('source/27-A-12.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.append(a[0])
s1 = sum(a[1:n//2])
s2 = sum(a[n//2+1:-1])
# print(a)
# print(s1, s2)
min_sum = 10000000000
for i in range(1, n // 2):
    s1 = s1 - a[i] + a[i + n // 2 - 1]
    s2 = s2 - a[i + n // 2] + a[i - 1]
    min_sum = min(min_sum, s1 + s2)
    # print(s1, s2)
    # print(a[i], a[i + n // 2 - 1], a[i + n // 2], a[i - 1])
print(min_sum)