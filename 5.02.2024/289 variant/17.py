with open('source/17-33.txt') as f:
    s = [int(x) for x in f]
    A = -10000
    mel = max([x for x in s if 10 <= abs(x) <= 99])
    for i in range(0, len(s) - 3):
        if abs(s[i])%10 == abs(s[i+1])%10 == abs(s[i+2])%10 == abs(s[i+3])%10:
            A = max(A, s[i] + s[i+1] + s[i+2] + s[i+3])
    a = []
    for i in range(0, len(s) - 4):
        if (((s[i] < A) + (s[i+1] < A) + (s[i+2] < A) + (s[i+3] < A) + (s[i+4] < A)) == 1) and ((s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4]) % mel == 0):
            a.append(s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4])
print(len(a), min(a))