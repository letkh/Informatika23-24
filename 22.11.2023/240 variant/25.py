i=12345078

#Вместо звёздочки ноль разрядов
if i%23==0:
    print(i, i//23)

for x in '0123456789':
    for y in '0123456789':
        s = '12345' + x + '7' + y + '8'
        i=int(s)
        if i%23==0:
            print(i, i//23)