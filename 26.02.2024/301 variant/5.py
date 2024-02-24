def f(n):
    n_bin = format(n, 'b')
    ost = format(n % 4, 'b')
    s = f'{n_bin}{ost}'
    return int(s, 2)

# print(f(30000002))
# print(f(894728061))
# print(abs(500000000 - 894728061) + 1)
a = []
c = 0
for i in range(400000000, 500000000):
    if 1_000_000_000 <= f(i) <= 1_789_456_123:
        c += 1
        a.append(f(i))
# for i in range(880000000, 894728061 + 1):
#     if 1_000_000_000 <= f(i) <= 1_789_456_123:
#         c += 1
#         a.append(f(i))
# print(a)
print(c)

# for i in range(500000000, 894728061):
#     if 1_000_000_000 <= f(i) <= 1_789_456_123:
#         print(i)
#         a.append(f(i))
# print(len(a))