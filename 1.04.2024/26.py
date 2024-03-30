f = open('source/26.txt')
n, m = map(int, f.readline().split())
a, b = [], []
for i in range(n):
    x, y = f.readline().split()
    match y:
        case 'A':
            a.append(int(x))
        case 'B':
            b.append(int(x))
res = []
print(res)