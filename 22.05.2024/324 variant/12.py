s = '9' * 98
while '4444' in s or '999' in s:
    if '4444' in s:
        s = s.replace('4444', '9', 1)
    else:
        s = s.replace('999', '4', 1)
print(s)