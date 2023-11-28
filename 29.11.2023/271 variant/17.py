a = []
for x in range(1157, 9932):
    if x % 2 == 0 and x % 3 != 0 and x % 7 != 0 and x % 8 != 0 and x % 11 != 0:
        a.append(x)
sorted(a)
print(len(a), a[len(a)-30])