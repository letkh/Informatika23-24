maxC = 0
count = 0
b = True
c =''
with open('source/24-5.txt') as f:
    s = f.readline()
for i in s:
    c = c + i
    if c.count('A') <= 1 and c.count('B') <= 1:
        count +=1
    else:
        maxC = max(maxC,count)
        count = 0
        c =''
print(maxC)
