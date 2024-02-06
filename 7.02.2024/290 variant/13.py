from ipaddress import ip_network

net = ip_network('23.140.159.160/255.255.252.0', strict=False)
c = 0

for a in net:
    a2 = format(a, 'b')
    if a2[:16].count('1') >= a2[-16:].count('1'):
        c += 1

print(c)