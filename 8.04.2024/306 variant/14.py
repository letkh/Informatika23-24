for m in range(11, 100):
    a = int('36620', m)
    b = int('51045', m)
    c = int('A33A4', m)
    d = int('12AA09', m)
    if a + b + c == d:
        print(m)
        break