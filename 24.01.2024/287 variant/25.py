from fnmatch import fnmatch
for i in range(163, 10**9, 163):
    if fnmatch(str(i), '3261??64*'):
        print(str(i), i // 163)