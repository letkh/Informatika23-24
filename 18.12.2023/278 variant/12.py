def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False    

    return True

def sum_stroki(n):
    s = 0
    intn = int(n[:-1])
    while intn > 0:
        s += intn % 10
        intn //= 10
    return s

for n in range(1, 100):
    s = '>' + '0' * 56 + '1' * 49 + '2' * n
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '12>')
        if '>2' in s:
            s = s.replace('>2', '5>')
        if '>0' in s:
            s = s.replace('>0', '22>')
    if isPrime(sum_stroki(s)):
        print(n)