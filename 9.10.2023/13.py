from ipaddress import ip_network
net = ip_network('202.75.38.176/255.255.255.240')
k = 0;
for address in net:
    bin_address = format(address, 'b')
    if ('111' not in bin_address) or ('000' not in bin_address):
        print(bin_address)
        k += 1
print(k)