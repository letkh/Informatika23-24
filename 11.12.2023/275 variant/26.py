f = open('source/26-1.txt').readlines()[1:]
f = sorted([list(map(int, i.split())) for i in f], key=lambda x: x[1])
otv1 = [f[0]]
for x in f[1:]:
    if x[0] > otv1[-1][1] + 15:
        otv1 += [x]
f = list(filter(lambda x: x[0] > otv1[-2][1] + 15, f))
print(len(otv1), max(i[0] - otv1[-2][1] for i in f))