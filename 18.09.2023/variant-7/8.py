def DecToQuad(n):
    b = ''
    while n > 0:
        b = str(n % 4) + b
        n = n // 4
    return b;
count = 0;

def IsDec(n):
    if ((n[0] >= n[1]) and (n[1] >= n[2])):
        return 1
    else:
        return 0

arr = []
for n in range(999):
    if len(DecToQuad(n)) != 3:
        continue
    else:
        a = DecToQuad(n)
        if IsDec(a):
            arr.append(a)
            count += 1;
print(arr)
print(count)