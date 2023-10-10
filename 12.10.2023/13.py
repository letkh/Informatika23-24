from ipaddress import ip_network

net = ip_network('202.75.38.160/255.255.255.240')
k = 0
for address in net:
    address_bin = format(address, 'b')
    if '111' in address_bin:
        k += 1
        print(address_bin)

print(k)
