from ipaddress import ip_network

net = ip_network('136.36.240.16/255.255.255.248')
c = 0
for a in net:
    a2 = format(a, 'b')
    if '101' not in a2:
        c += 1

print(c)