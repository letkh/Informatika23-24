c = 0
for i in range(1, 1000000):
    if len(format(i, 'o')) == 5:
        if format(i, 'o').count('1') == 0 and \
                len(list(format(i, 'o'))) == len(list(set(list(format(i, 'o'))))) and \
                int(format(i, 'o')[0]) % 2 != int(format(i, 'o')[1]) % 2 and \
                int(format(i, 'o')[1]) % 2 != int(format(i, 'o')[2]) % 2 and \
                int(format(i, 'o')[2]) % 2 != int(format(i, 'o')[3]) % 2 and \
                int(format(i, 'o')[3]) % 2 != int(format(i, 'o')[4]) % 2:
            c += 1
print(c)
