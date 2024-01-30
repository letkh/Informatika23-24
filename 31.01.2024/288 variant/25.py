from fnmatch import fnmatch

for i in range(0, 2 * 10 ** 8, 42):
    if fnmatch(str(i), '?2*4*0') and not fnmatch(str(i), '1*7*'):
        print(i, i//42)