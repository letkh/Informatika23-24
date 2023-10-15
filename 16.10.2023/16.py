for x in range(1, 10000):
    a_dec = 125 ** 7 - 25 ** 4 + x
    a_fifth = ''
    while a_dec > 0:
        a_fifth = f'{a_dec % 5}{a_fifth}'
        a_dec //= 5
    if a_fifth.count('4') == 15 and a_fifth.count('3') == 1 and a_fifth.count('1') == 2:
        print(x)
        break