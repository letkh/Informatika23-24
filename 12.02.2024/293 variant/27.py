import math

f = open('source/27_B.txt')
n, m = f.readline().split()
n = int(n)
m = int(m)
capacity = 20
a = [0]*100000000
for line in f:
    distance, elaboration = map(int, line.split())
    a[distance] = math.ceil(elaboration / capacity)
current_canisters = 0
for i in range(m * 2 + 1):
    if i < m * 2:
        current_canisters += a[i]
max_canisters = 0
for i in range(m + 1, len(a) - m):
    current_canisters = current_canisters - a[i - m - 1] + a[i + m]
    if a[i] != 0:
        max_canisters = max(max_canisters, current_canisters)
print(max_canisters)