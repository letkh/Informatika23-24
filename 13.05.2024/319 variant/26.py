f = open('source/26.txt')
n = int(f.readline().strip())
shift_length = 14 * 60
data = []
for i in range(n):
    line = sum(map(int, f.readline().split()))
    if line == 203:
        print(i)
    data.append(line)
data.sort()
res = [data[0]]
i = 1
while i < n - 1:
    if sum(res) + data[i] <= shift_length:
        res.append(data[i])
    i += 1
print(sum(res), res)