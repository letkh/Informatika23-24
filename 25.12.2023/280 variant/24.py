f=open('source/24-7.txt')
s= f.readline()
f.close()
k=0
b=[]

for i in range(len(s)):
    if s[i] == 'A':
        k=1
        for j in range(i+1, len(s)):
            if s[j] == 'A':
                k += 1
            if k == 350:
                b.append(j-i+1)
                break         

print(max(b))