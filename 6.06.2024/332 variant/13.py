from ipaddress import ip_network
net = ip_network('124.6.102.0/255.255.254.0', 0)
b = []
for a in net:
    a2 = format(a, 'b')
    b.append(a2.count('0'))
print(max(b))