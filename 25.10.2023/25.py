count = 0
i = 10000001
while count < 5:
    halfI = i // 2
    dell = 0
    countDel = 0
    for j in range(halfI, 1, -1):
        if i % j == 0:
            countDel += 1
            dell += j
            if dell > 10000:
                break
            elif countDel == 2:
                print(dell)
                count += 1
                break
    i += 1