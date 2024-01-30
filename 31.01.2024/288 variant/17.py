with open('source/17-32.txt') as f:
    s = [int(x) for x in f]
    a = []
    for i in range(len(s) - 5):
        x, y, z = s[i]+s[i+1], s[i+2]+s[i+3], s[i+4]+s[i+5]
        if x > 0 and y > 0 and z > 0 and y > x and y > z:
            a.append(s[i+2]*s[i+3])

print(len(a), min(a))