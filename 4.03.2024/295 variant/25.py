import fnmatch

for i in range(0, 10 ** 8):
    if fnmatch.fnmatch(str(i), '*15*7424') and ((i % 111 == 0) + (i % 113 == 0) + (i % 127 == 0)) == 1:
        print(i, i / 111, i / 113, i / 127)