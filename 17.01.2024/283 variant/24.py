f = open('source/24-11.txt')
s = f.readline()
s = s.replace('0', '!')
s = s.replace('1', '*')
s = s.replace('2', '*')
s = s.replace('3', '*')
s = s.replace('4', '*')
s = s.replace('5', '*')
s = s.replace('6', '*')
s = s.replace('7', '*')
s = s.replace('8', '*')
s = s.replace('9', '*')
s = s.replace('A', '*')
s = s.replace('B', '*')
s = s.replace('C', '*')
s = s.replace('D', '*')
s = s.replace('E', '*')
s = s.replace('F', '*')

k = 0
mk = 0
for i in s:
    if (i == '!' and k != 0) or i == '*':
        k += 1
        mk = max(k, mk)
    else:
        k = 0
    

print(mk)