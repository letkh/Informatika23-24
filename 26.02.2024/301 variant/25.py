from fnmatch import fnmatch

for i in range(1987, 10**10, 1987):
    if fnmatch(str(i), '1*4022?9'):
        print(i, i // 1987)