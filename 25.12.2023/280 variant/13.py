from ipaddress import *
net = ip_network('116.29.170.89/255.255.255.224', 0)
k = 0
for ip in net:
    ip_bin = f'{ip:b}'
    if ip_bin[:16].count('1') >= ip_bin[16:].count('1'):
        k += 1
print(k)