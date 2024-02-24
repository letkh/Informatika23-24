f = open('source/27-B.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort(reverse=True)
multiply = a[0]
for i in range(n):
    if multiply * a[i] % 55 == 0:
        print(multiply * a[i])
        break