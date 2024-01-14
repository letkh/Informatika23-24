def f(s):
    while '00' not in s:
        s = s.replace('01', '220', 1)
        s = s.replace('02', '1013', 1)
        s = s.replace('03', '120', 1)
    return s

for x in range(1, 50):
    for y in range(1, 50):
        for z in range(1, 50):
            s = f('0' + '1' * x + '2' * y + '3' * z + '0')
            if s.count('1') == 13 and s.count('2') == 18:
                print('1 -', x)
                print('2 -', y)
                print('3 -', z)
                print(x + y + z + 2)