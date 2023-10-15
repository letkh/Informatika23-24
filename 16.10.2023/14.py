#import collections

a = 2 ** 51 + 2 ** 40 + 2 ** 35 + 2 ** 17 - 2 ** 5
list = []
while a > 0:
    list.append(a % 16)
    a //= 16

#freq = collections.Counter(list) 
#print(freq)

print(len(set(list)))