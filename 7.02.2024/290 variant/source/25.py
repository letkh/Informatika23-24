from fnmatch import fnmatch

for i in range(5171, 10 ** 8, 5171):
    if fnmatch(str(i), '?19*8?3'):
        print(i, i // 5171)