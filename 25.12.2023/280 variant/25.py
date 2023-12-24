from fnmatch import *
for x in range(0, 10 ** 10, 12007):
    s = str(x)
    if fnmatch(s, '9*?001?1'): print(x, x // 12007)