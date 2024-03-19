f = open('source/26.txt')
n, m = map(int, f.readline().split())
red, blue = [], []

for i in range(min(n, m)):
    line = f.readline().split()
    red.append(int(line[0]))
    blue.append(int(line[1]))

for i in range(min(n, m), max(n, m)):
    line = f.readline().split()
    blue.append(int(line[0]))

red.sort(reverse=True)
blue.sort(reverse=True)
res = [['b', blue[0]]]
for i in range(max(n, m)):
    if res[i][0] == 'r':
        if not [x for x in blue if res[i][1] - x >= 5]:
            break
        res.append(['b', max([x for x in blue if res[i][1] - x >= 5])])
    else:
        if not [x for x in red if res[i][1] - x >= 5]:
            break
        res.append(['r', max([x for x in red if res[i][1] - x >= 5])])
print(res)
print(len(res), res[-1][1])