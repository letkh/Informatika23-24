import collections

a = 9 ** 5 + 3 ** 7 - 14
list = []
k = 0

while a > 0:
    list.append(a % 3)
    a //= 3

freq = collections.Counter(list) 
print(freq)