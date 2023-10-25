f = open("source/27-B.txt")
n = int(f.readline())
lefts = [0 for i in range(30)]
maxsum = 0
for i in range(30):
    lefts[i] = 2 * 1000000000
    count = 0
    sum = 0
for i in range(1, n + 1):
    num = int(f.readline())
    sum = sum + num
    if (num % 2 == 0) and (num > 0):
        count = count + 1
    d = count % 30
    if sum < lefts[d]:
        lefts[d] = sum
    maxsum = max(maxsum, sum - lefts[d])
print(maxsum)