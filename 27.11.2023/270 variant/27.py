with open('source/27_A.txt') as f:
    s,d = f.readline().split()
    g = [int(x) for x in f]
    
count = 0
mx = 0
for i in range(0, int(s)-30):
    a = sorted(g[i+30:], reverse=True)[0]
    if (int(g[i]) + a) % 3 == 0:
        mx = max(mx, g[i] + a)
        
print(mx)