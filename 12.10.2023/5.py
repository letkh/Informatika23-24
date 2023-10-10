def f(n):
    n_bin = format(n, 'b')
    s = n_bin[:-2]
    return int(s, 2)
list = []
for n in range(20, 601):
    list.append(f(n))
print(len(set(list)))
