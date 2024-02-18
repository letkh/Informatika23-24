f = open('source/27-A.txt')
n = int(f.readline())
a = [int(x) for x in f]
max_sum = 0
max_count = 0
count = 0
for i in range(n):
    cur_sum = 0
    count = 0
    for j in range(i, n):
        cur_sum += a[j]
        count += 1
        if cur_sum >= max_sum and cur_sum % 113 == 0:
            max_sum = max(max_sum, cur_sum)
            max_count = max(max_count, count)
print(max_count)