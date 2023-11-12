f=open('source/24.txt')
s=f.read()
k=1
kmax=0

for i in range(0, len(s)-1):
    if s[i]<=s[i+1]:
        k=k+1
        kmax=max(k, kmax)
    else:
        k=1

print(kmax)