from ipaddress import ip_network
k = 0
net = ip_network('192.168.32.160/255.255.255.240')
for add in net:
    add_bin = format(add, 'b')
    if add_bin.count('1') % 2 == 0:
        k += 1
        print(add_bin)

print(k)