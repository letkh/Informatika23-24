
s=open('source/24-2.txt').read()
s=s.split('A')
k=m=0
for x in range(len(s)):
    if s[x].count('E')>2:
        k=len(s[x])
        m=max(m,k)
print(m)