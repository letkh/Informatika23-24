from fnmatch import fnmatch
for i in range(0, 10 ** 10, 48910):
    if fnmatch(str(i), '3*566?6?'):
        print(i, i//48910)