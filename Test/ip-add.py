import ipaddress

x = [str(ip) for ip in ipaddress.IPv4Network('192.168.2.0/28')]
print(x)
