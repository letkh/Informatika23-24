f=open('source/24-3.txt')
s=f.read()
k=1
kmax=0

for i in range(1, len(s)-2):
    if s[i]<=s[i+1]:
        s1 = s[i-1]
        s2 = s[i+2]
        k=k+1
        if (s1 == s2):
            kmax=max(k, kmax)
    else:
        k=1

print(kmax)