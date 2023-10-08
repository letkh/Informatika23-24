def f(n):
    n_bin = format(n, 'b');
    s = '';
    if n_bin.count('1') % 2 == 0:
        s = '{}1{}'.format(n_bin[:len(n_bin) // 2], n_bin[len(n_bin) // 2:])
    else:
        s = n_bin
    return int(s, 2)

for n in range(0, 100):
    if f(n) > 26:
        print(n);
        break;