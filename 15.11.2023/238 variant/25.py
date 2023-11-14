def delit(a) :
    res = []
    i = 1
    while i * i < a + 1 :
        if a % i == 0 :
            res.append(i)
            if i != a // i :
                res.append(a // i)
        i += 1
    return sorted(res)

for x in range(3954, 8979):
    if 41 <= len(delit(x)) <= 45:
        print(x, len(delit(x)))