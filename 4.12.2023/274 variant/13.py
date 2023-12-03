from ipaddress import ip_network
k = 0
net = ip_network('142.108.56.118/255.255.255.240', strict=False)
for ad in net:
    ad_bin = format(ad, 'b')
    if ad_bin[:16].count('1') < ad_bin[-16:].count('1'):
        k += 1

print(k)