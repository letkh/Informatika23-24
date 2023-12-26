from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '3?2258*4'):
        print(x)