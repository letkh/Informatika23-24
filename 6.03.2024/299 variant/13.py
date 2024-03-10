from ipaddress import ip_network

net = ip_network('202.75.38.176/255.255.255.240', 0)
c = 0
for a in net:
    a2 = format(a, 'b')
    if '000' not in a2 and '111' not in a2:
        c += 1
print(c)