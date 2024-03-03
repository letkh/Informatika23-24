import ipaddress
net = ipaddress.ip_network('252.67.33.87/255.252.0.0', 0)
print(len([a for a in net if format(a, 'b')[:16].count('1') * 2 < format(a, 'b')[16:].count('1')]))