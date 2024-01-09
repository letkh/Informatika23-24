s = open('source/24-9.txt').readline()
while 'NYNYN' in s:
    s = s.replace('NYNYN', 'NYN NYN')
s = s.replace('NYN', 'HPY')
i = 1
while i * 'HPY' in s:
    i += 1
print(i-1)