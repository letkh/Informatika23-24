def uniq(num):
    return len(set(list(str(num)))) == 6

def count(num, param):
    a = 0;
    b = 0;
    while num > 0:
        if num % 2 == 0:
            a += 1
        else:
            b += 1
        num //= 10
    if (param):
        return a
    else:
        return b
k = 0;
for i in range(99999, 999999):
    if (i % 100 == 26) and (uniq(i)) and ((count(i, True) == 3) or (count(i, False) == 2)):
         k += 1
         print(i)
print(k)