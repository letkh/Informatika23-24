from ipaddress import ip_network
net = ip_network('105.224.200.224/255.255.255.224')
c = 0
for a in net:
    if format(a, 'b').count('1') % 4 == 0:
        c += 1
print(c)