import collections

a = 343 ** 1515 - 6 * 49 ** 1520 + 5 * 49 ** 1510 - 3 * 7 ** 1530 - 1550
list = []
while a > 0:
    list.append(a % 7)
    a //= 7

freq = collections.Counter(list) 
print(freq)