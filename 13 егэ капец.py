#from ipaddress import *
#net=ip_network('192.168.10.100/255.255.255.0',0)   # адрес сети
#for ip in net.hosts(): # хост чтобы убрать первые и последние строки, которые не \
    #подходят
#    print(ip)
#print(net)


#print(a:=198, f'В двоичной: {a:b}')

#k=0
#net=ip_network('172.16.168.0/255.255.248.0',0)
#for ip in net:
#    if f'{ip:b}'.count('1') %5!=0:
 #       k+=1
#print(k)     

#from ipaddress import *
#net=ip_network('98.71.254.171/255.248.0.0',0)
#print(net)
#for ip in net:
#    if f'{ip:b}'.zfill(32).count('1')%7==0:
#        print(ip)
#        break

#from ipaddress import *

#for mask in range(32,0,-1):
 #   net1=ip_network(f'161.137.200.35/{mask}',0)
#    net2=ip_network(f'161.137.150.118/{mask}',0)
#    if net1==net2:
#        a=[1 for ip in net1 if f'{ip:b}'.zfill(32).count('1')%2!=0]
#        break
#print(sum(a))
#for mask in range(32,0,-1):
 #   net1=ip_network(f'176.213.225.119/{mask}',0)
 #   net2=ip_network(f'176.213.195.58/{mask}',0)
 #   if net1==net2:
 #       print(net1.netmask)


#for mask in range(32,0,-1):
#    net=ip_network(f'180.2.252.76/{mask}',0)
#    if net.network_address==ip_address('180.2.224.0'):
#        print(net.netmask)



#from ipaddress import *
#net=ip_network('172.95.116.174/255.255.192.0',0)
#for ip in net:
#    if f'{ip:b}'.zfill(32).count('1')%5==0:
#        print(ip)
 #       break


#from ipaddress import *
#net=ip_network('73.148.145.65/255.224.0.0',0)
#for ip in net.hosts():
#    print(net[-2])
#    break


#from ipaddress import *
#net=ip_network('98.71.254.171/255.248.0.0',0)
#for ip in net:
 #   if f'{ip:b}'.zfill(32).count('1')%7==0:
 #       print(ip)
 #       break


#from ipaddress import *
#for mask in range(32,-1,-1):
 #   net=ip_network(f'84.23.84.23/{mask}',0)
#    if net.network_address==ip_address('84.23.84.0'):
 #       print(net.netmask)
    
#from ipaddress import *
#for mask in range(0,33):
#    net=ip_network(f'84.32.84.32/{mask}',0)
#    if f'{net[-2]:b}'.count('1')==19:
 #       print(mask)
 #       break















 
