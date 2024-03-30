from fnmatch import fnmatch

for i in range(0, 10 ** 8, 323):
    if fnmatch(str(i), '2*8?6?13'):
        print(i, i//323)