import math

f = open('source/27_A-14.txt')
n, m = f.readline().split()
n = int(n)
m = int(m)
capacity = 20
a = []
for i in range(n):
    line = f.readline()
    number, quantity = line.split()
    amount_canister = math.ceil(int(quantity) / capacity)
    a.append([int(number), amount_canister])
tmp_array = [x[0] for x in a]
for i in range(tmp_array[len(tmp_array) - 1]):
    if i not in tmp_array:
        a.append([i, 0])
a.sort(key=lambda x: x[0])
left_part = 0
right_part = 0
for i in range(m):
    left_part = left_part + a[i][1]
for i in range(m+1, m*2+1):
    right_part = right_part + a[i][1]
max_canisters = right_part + left_part + a[m][1]

for i in range(m + 1, a[len(a) - 1][0] - m):
    left_part = left_part - a[i - m - 1][1] + a[i - 1][1]
    right_part = right_part - a[i][1] + a[i + m][1]
    if a[i][1] != 0:
        max_canisters = max(max_canisters, left_part + right_part + a[i][1])

print(max_canisters)