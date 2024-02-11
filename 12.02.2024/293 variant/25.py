from fnmatch import fnmatch

for i in range(0, 10**8, 123):
    if fnmatch(str(i), '32*823'):
        print(i, i//123)