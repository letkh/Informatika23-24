s = '7' * 112

while '111' in s or '7777' in s:
    if '111' in s:
        s = s.replace('111', '7', 1)
    else:
        s = s.replace('7777', '1', 1)
print(s)