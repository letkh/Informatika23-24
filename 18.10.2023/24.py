with open('source/24-1.txt', 'r') as f:
    a = [line.split() for line in f]
    min = 10000
    for x in a:
        for i in range(0, len(x)):
            if len(x[i]) < min:
                min = len(x[i])
print(min)