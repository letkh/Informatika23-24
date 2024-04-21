def prefix_sum_array(arr):
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)
    return prefix_sum

f = open('source/27_B-7.txt')
n, m = map(int, f.readline().split())
m = m // 8
a = [0]*n
ms = 0
res = []
for i in range(n):
    a[i] = int(f.readline().strip())
a = a[-m:] + a + a[:m]
ps = prefix_sum_array(a)
for i in range(n - (2 * m)):
    s = ps[i + (2 * m) + 1] - ps[i]
    if ms != max(s, ms):
        res.append(i)
    ms = max(s, ms)

print(max(res) * 8)