s = open('source/24-27.txt').readline()
n = 'abcdefg'
for l in n:
    for i in range(1, 1000):
        if l*i in s and l*(i + 1) not in s:
            s = s.replace(l*i, f'{l}{i - 2}{l}')
res = []
for i in range(len(s) - 2):
    if s[i].isdigit():
        if s[i-2] != s[i + 2]:
            res.append(int(s[i]) + 2)
print(max(res))

# я чуть не умер, пока это писал
# в общем, ищем повторяющиеся символы,
# затем заменяем их внутренность на количество,
# например, aaaa -> a2a. так можно будет отследить
# крайние символы, и проверить их равенство
