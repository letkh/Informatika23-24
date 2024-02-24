from fnmatch import fnmatch

for i in range(0, 10 ** 9, 149):
    if fnmatch(str(i), '1840?9*6'):
        print(i, i//149)