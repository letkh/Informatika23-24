def f(n):
    n_bin = format(n, 'b')
    s = ''
    if n % 2 == 0:
        s = '1' + n_bin + '10'
    else:
        s = '11' + n_bin + '0'
    return int(s, 2)

lst = []
for i in range(800, 1501):
    lst.append(f(i))

print(len(set(lst)))