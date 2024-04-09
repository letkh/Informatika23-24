from fnmatch import fnmatch

for i in range(0, 10 ** 10, 34260):
    if fnmatch(str(i), '521*4*33*'):
        print(i, i // 34260)