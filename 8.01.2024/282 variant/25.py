from fnmatch import fnmatch
for i in range(3057, 10 ** 9 + 1, 3057):
    if fnmatch(str(i), '1?58*5?9'):
        print(i, i//3057)