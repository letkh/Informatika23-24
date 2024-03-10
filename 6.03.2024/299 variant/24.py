f = open('source/24-21.txt')
res = 0
s = f.readline().split('A')
for i in range(len(s)-5):
    res = max(len(s[i])+len(s[i+1])+len(s[i+2])+len(s[i+3])+len(s[i+4])+len(s[i+5])+5,res)
print(res)