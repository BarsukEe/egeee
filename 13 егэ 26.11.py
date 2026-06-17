from ipaddress import *
#k=0
#mn=1000
#for mask in range(32,16,-1):
#    net1=ip_network(f'163.135.196.55/{mask}',0)
#    net2=ip_network(f'163.135.210.181/{mask}',0)
#    if net1==net2:
 #       for ip in net1:
 #           if f'{ip:b}'.count('1')==21:
  #              k+=1
   #         if k>mn:
    #            break
     #   if k<mn:
     #       mn=k
      #  print(mn)  
       # k=0
for mask in range(32,-1,-1):
    net=ip_network(f'193.18.135.201/{mask}',0)
    if net.num_addresses==105:
        print(net)
