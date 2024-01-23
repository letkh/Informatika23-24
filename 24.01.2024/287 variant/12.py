s = '>' + 15 * '2' + 20 * '3' + 25 * '5'

while '>2' in s or '>3' in s or '>5' in s:
    if '>2' in s:
        s = s.replace('>2', '333>', 1)
    if '>3' in s:
        s = s.replace('>3', '23>', 1)
    if '>5' in s:
        s = s.replace('>5', '35>', 1)
sum = 0
s = int(s[:-1])
while s > 0:
    sum += s % 10
    s //= 10
print(sum)