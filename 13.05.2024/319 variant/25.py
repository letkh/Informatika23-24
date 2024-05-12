from fnmatch import fnmatch
for i in range(0, 10 ** 11, 58476):
    if fnmatch(str(i), '*27?3981?'):
        print(i, i//58476)