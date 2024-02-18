from ipaddress import ip_network

net = ip_network('192.168.32.48/255.255.255.240', 0)
c = 0
for a in net:
    a2 = f'{a:b}'
    if a2.count('1') % 2 != 0:
        c +=1
print(c)