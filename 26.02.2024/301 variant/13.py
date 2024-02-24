print(format(19, 'b'))
print(format(57, 'b'))
print(int('11000000', 2))
from ipaddress import ip_network

net = ip_network('114.91.0.39/255.255.192.0', 0)
c = 0
for a in net:
    a2 = format(a, 'b')
    if a2.count('1') % 2 == 0:
        c += 1

print(c)