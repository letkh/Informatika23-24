s = open('source/24.txt').readline().split('Y')
ml = 0
for i in range(len(s)-150):
    st = 'Y'.join(s[i:i+151])
    if ml < len(st):
        ml = len(st)
print(ml)