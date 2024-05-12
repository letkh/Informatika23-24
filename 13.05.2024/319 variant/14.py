import string
n = string.digits + string.ascii_uppercase[:3]
for x in range(0, 13):
    if all((int(f'CC68{x}{y}', 13) + int(f'2{y}343{x}7', 13)) % 7 == 0 for y in range(0, 13)):
        print(x)
x = 0
y = 3
print(int(f'CC68{x}{y}', 13) + int(f'2{y}343{x}7', 13) / 7)