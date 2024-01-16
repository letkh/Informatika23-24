from ipaddress import *
c = 0
net = ip_network('192.168.32.160/255.255.255.240')
for a in net:
    a_bin = format(a, 'b')
    if a_bin.count('0') > 21:
        c += 1
print(c)    