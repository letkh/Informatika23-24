f = open('source/26.txt')
n, m = map(int, f.readline().split())
boxes, keys, valid_pair = [], [], []

for i in range(min(n, m)):
    line = f.readline().split()
    boxes.append(int(line[0]))
    keys.append(int(line[1]))

for i in range(min(n, m), max(n, m)):
    line = f.readline().split()
    boxes.append(int(line[0]))

for key in keys:
    if key in boxes:
        valid_pair.append(key)

valid_pair.sort(reverse=True)
c = 1
res = [valid_pair[0]]
for i in range(1, len(valid_pair)):
    if res[-1] - valid_pair[i] >= 6:
        c += 1
        res.append(valid_pair[i])
print(c, min(res))