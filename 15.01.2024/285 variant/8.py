from itertools import product

even = '2468'
odd = '1357'
count = 0
for i in product(even, repeat = 5):
    if ''.join(i).count(i[0]) <= 4:
        for j in product(odd, repeat = 6):
            if ''.join(j).count(j[0]) <= 4 and ''.join(j).count(j[1]) <= 4:
                count += 1
print(count * 2)
