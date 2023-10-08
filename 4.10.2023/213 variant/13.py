from ipaddress import ip_network
net = ip_network("192.168.248.176/255.255.255.240", strict=False)
bin_addresses = [f"{address:b}" for address in net]
c = 0
for address in bin_addresses:
    if address.count("1") > address.count("0"):
        print(address)
        c += 1
print(c)