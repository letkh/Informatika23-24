f = open("source/27_A-21.txt")
n = int(f.readline().strip())
k = int(f.readline().strip())
a = [int(x) for x in f]
count = 0
for i in range(n - 1):
    p = k - a[i]
    if a[-1] - k <= a[i]:
        left = i
        right = n - 1
        while left != right - 1:
            center = (left + right) // 2
            if a[center] < p:
                left = center
            else:
                right = center
        count += n - right
print(count)