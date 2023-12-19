f=open('source/24-6.txt')
s=f.read()
sum=0
for i in range(len(s)-3):
    if s[i] not in '0123456789' and s[i+1] in '0123456789' and s[i+2] in '0123456789' and s[i+3] in '0123456789' and s[i+4] not in '0123456789':
        sum += int(f'{s[i+1]}{s[i+2]}{s[i+3]}')

print(sum)