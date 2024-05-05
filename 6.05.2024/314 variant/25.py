from fnmatch import fnmatch
for i in range(0, 10**10, 2024):
    if fnmatch(str(i), '1*2322?2'):
        print(i, i//2024)