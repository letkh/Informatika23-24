f = open('source/26-11.txt')
n = f.readline()
a = [int(x) for x in f]
a.sort(reverse=True)
distance_now = a[0]
c = 1
b = []

for i in range(1,len(a)):
    if distance_now - a[i] >= 6:
        distance_now = a[i]
        b.append(distance_now)
        c += 1
print(c, min(b))