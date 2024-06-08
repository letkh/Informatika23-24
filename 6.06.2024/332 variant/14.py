import string
n = string.digits + string.ascii_uppercase[:11]
for x in n:
    if all((int(f'1325{y}{x}69', 21) + int(f'32615{y}799', 21)) % 18 == 0 for y in n):
        print(x)

x = 'K'
y = '5'
print((int(f'1325{y}{x}69', 21) + int(f'32615{y}799', 21)) // 18)