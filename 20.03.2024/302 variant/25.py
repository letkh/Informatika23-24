from fnmatch import fnmatch

for i in range(0, 10 ** 9, 2049):
    if fnmatch(str(i), '32*21?4'):
        print(i, i//2049)