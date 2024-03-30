from ipaddress import ip_network

net = ip_network('222.63.131.128/255.255.255.192', 0)
c = 0
for a in net:
    a2 = format(a, 'b')
    if a2.count('1') % 5 == 0:
        c += 1
print(c)