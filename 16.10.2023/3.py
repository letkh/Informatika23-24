import collections

a = 9 ** 17 + 3 ** 16 - 27
list = []
k = 0

while a > 0:
    list.append(a % 3)
    a //= 3

freq = collections.Counter(list) 
print(freq)