s = '>' + '2' * 12 + '3' * 22 + '5' * 15

while ('>2' in s) or ('>3' in s) or ('>5' in s):
    if '>2' in s:
        s = s.replace('>2', '55>', 1)
    if '>3' in s:
        s = s.replace('>3', '523>', 1)
    if '>5' in s:
        s = s.replace('>5', '52>', 1)

print(s)

sum = 0
for a in s: 
    if a.isdigit(): 
        sum += int(a)

print(sum)