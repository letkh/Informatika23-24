f = open('source/26-12.txt')
n, m = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort()
b = [a[0]]
throughput_capacity, max_width = 0, 0
for i in range(1, len(a)):
    if len(b) < m:
        if abs(b[-1] - a[i]) <= 3:
            b.append(a[i])
        else:
            b = [a[i]]
    elif abs(b[-1] - a[i]) <= 3 and b[-1] == a[i]:
        b.append(a[i])
        b.pop(0)
    else:
        print(b)
        print(b[0], b[-1])
        b = [a[i]]