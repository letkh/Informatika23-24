s = open('source/24-19.txt').readline()
# s = s.split('A')
# mc = 100000
# for i in range(len(s) - 34):
#     c = 1
#     for j in range(i, i + 34):
#         c += 1 + len(s[j])
#     mc = min(mc, c)
#
# print(mc)
a = 0
c = 0
mc = 100000

for i in range(len(s)):
    if s[i] == 'A':
        a += 1
        c += 1
        if a > 35:
            mc = min(c, mc)
            a = 0
            c = 0
    else:
        c += 1
print(mc)
