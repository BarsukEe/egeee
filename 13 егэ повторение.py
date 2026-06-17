from ipaddress import *
for A in range(256):
    net=ip_network(f'159.242.{A}.223/255.255.254.0',0)
    if sum(1 for ip in net if f'{ip:b}'[:16].zfill(32).count('0')< \
     f'{ip:b}'[16:].zfill(32).count('0'))==net.num_addresses:
        print(A)
