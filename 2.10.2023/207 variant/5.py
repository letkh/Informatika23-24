def F(n):
    nBin = format(n, 'b');
    str = '';
    if (int(nBin) % 2 == 0):
        str = '{}{}'.format(nBin, '01')
    else:
        str = '{}{}{}'.format('1', nBin, '10')
    res = int(str, 2)
    return res

for n in range(0,200):
    if F(n) < 105:
        print(n)