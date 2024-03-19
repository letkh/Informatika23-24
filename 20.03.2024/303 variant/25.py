from fnmatch import fnmatch

for i in range(0, 10 ** 9, 2079):
    if fnmatch(str(i), '32*21?7'):
        print(i, i//2079)