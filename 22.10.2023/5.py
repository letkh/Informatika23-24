def f(n):
    if int(f'{int(str(n)[0]) + int(str(n)[1])}') < int(f'{int(str(n)[2]) + int(str(n)[3])}'):
        s = int(f'{int(str(n)[0]) + int(str(n)[1])}{int(str(n)[2]) + int(str(n)[3])}')
    else:
        s = int(f'{int(str(n)[2]) + int(str(n)[3])}{int(str(n)[0]) + int(str(n)[1])}')
    return s

for i in range(1000, 9999):
    if f(i) == 117:
        print(i)