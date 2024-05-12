import sympy
def get_divisors(number):
    result = {1, number}
    for divisor in range(2, number // 2  + 1):
      if number % divisor == 0:
          result.add(divisor)
    return sorted(result)
for i in range(550000, 1000000):
    if not sympy.isprime(get_divisors(i)[-2]):
        print(i, get_divisors(i)[-2])