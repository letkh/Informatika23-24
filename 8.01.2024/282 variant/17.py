data = [int(line) for line in open('source/17-27.txt')]
T = min(elem for elem in data if elem > 0 and elem % 117 == 0)
a = []
for i in range(len(data) - 1):
    if (data[i] < 0) != (data[i + 1] < 0) and (data[i] + data[i+1]) % T == 0:
        a.append(data[i] ** 2 + data[i+1] ** 2)
print(len(a), min(a))