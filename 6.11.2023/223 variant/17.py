a = [int(x) for x in open('source/17-17.txt')]
end = [x for x in a if x % 100 == 43]
res = []
min = min(end)

for i in range(len(a) - 1):
    if (a[i] + a[i+1] % min == 0) or ((str(a[i])[len(str(a[i]))-1] == str(min)[len(str(min))-1]) or (str(a[i + 1])[len(str(a[i + 1]))-1] == str(min)[len(str(min))-1])) == 1:
        res.append([a[i], a[i+1]])
print(len(res), max(res))