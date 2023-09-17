def sum(a):
    s = 0
    n = int(a)
    while n:
        s += n % 10
        n //= 10
    return s

for i in range(2, 100000):
        str = '5'+'2'*i;
        #print(str)
        while ('52' in str or '2222' in str or '1122' in str):
            if ('52' in str):
                str = str.replace('52', '11')
                #print(str)
            if ('2222' in str):
                str = str.replace('2222', '5')
                #print(str)
            if ('1122' in str):
                str = str.replace('1122', '25')
                #print(str)
        if sum(str) == 64:
            print(i)
print('Цикл закончен')