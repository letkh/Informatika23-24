from ipaddress import ip_network
net = ip_network('108.25.239.240/255.255.255.248', strict=False)
res = []
for a in net:
    a2 = format(a, 'b')
    if a2.count('0') % 3 == 0:
        res.append(a2)
print(len(res))