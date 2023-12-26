f = open('source/24-8.txt')
s = f.readline()
ind_ab = []
for i in range(len(s)):
    if s[i] in 'XY':
        ind_ab.append([i, s[i]])
max_len = 0
for i in range(len(ind_ab) - 3):
    if ind_ab[i+1][1] != ind_ab[i+2][1]:
        max_len = max(max_len, ind_ab[i+3][0] - ind_ab[i][0] - 1)
print(max_len)