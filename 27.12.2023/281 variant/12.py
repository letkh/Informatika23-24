def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def sum_digits(string):
    summa = 0
    for char in string:
        summa += int(char)
    return summa
c = []
for x in range(50):
    for y in range(50):      
        a = '0' + '1'*x + '2'*y
        while '01' in a or '02' in a:
            a = a.replace('02', '1110', 1)
            a = a.replace('01', '220', 1)
        if isPrime(sum_digits(a)) and x + y > 44:
            t = x * 1 + y * 2
            c.append(t)
print(min(c))