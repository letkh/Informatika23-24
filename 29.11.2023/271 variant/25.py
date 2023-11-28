i=1234506078

if i%19==0:
    print(i, i//19)

for x in '0123456789':
    for y in '0123456789':
        s = '12345' + x + '6' + y + '78'
        i=int(s)
        if i%19==0:
            print(i, i//19)