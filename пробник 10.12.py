
#from itertools import *
#s='25 134 246 235 147 37 56'.split()
#v='AB AC AD BG DF CF CE EF GE'.split()
#print(*range(1,8))
#for p in permutations('ABCDEFG'):
#    if all(str(p.index(b)+1 )in s[p.index(a)] for a,b in v):
#        print(*p)

#from itertools import *
#def f(x,y,w,z):
 #   return ((not(y<=x)) or ((not w) == (z<=y)) or z)
#for i in product([0,1],repeat=7):
 #   t=[(1,i[0],i[1],0),(i[2],i[3],0,1),(0,i[4],i[5],i[6])]
 #   if len(t)==len(set(t)):
 #       for p in permutations('xywz'):
 #          if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
 #               print(p)
#for n in range(4,100):
 #   b=bin(n)[2:]
 #   if n%2==0:
 #       b+=b[-2:]
  #  else:
   #     b+=b[-3:]
    #r=int(b,2)
    #if r>256:
     #   print(n,r)
#f=open('17var08.txt')
#a=[int(x) for x in f]
#k=0
#c=0
#md=-1000000
#minn=100000
#for i in range(len(a)):
#    if a[i]<minn:
#        minn=a[i]
#for i in range(len(a)-1):
#    if (((a[i]%33) + (a[i+1]%33))==minn):
#        k+=1
#        if abs(a[i]-a[i+1])>md:
#            md=(a[i]-a[i+1])
#print(k,md)


#from ipaddress import *
#k=0
#net=ip_network(f'63.7.215.0/255.255.252.0',0)
#for ip in net.hosts():
#    if f'{ip:b}'.zfill(32).count('1')%8!=0:
#        k+=1
#        print(k,ip)


#def f(s,m):
 #   if s<=34: return m%2==0
 #   if m==0: return 0
#    h=[f(s-3,m-1),f(s-7,m-1),f(s//4,m-1)]
#    return any(h) if m%2==0 else all(h)
#print('19',[s for s in range(35,10000) if not f(s,1) and f(s,2)])
#print('20',[s for s in range(35,10000) if not f(s,1) and f(s,3)])
#print('21',[s for s in range(35,10000) if not f(s,2) and f(s,4)])





from itertools import *
k=0
c=0
for w in product('123456',repeat=5):
    k+=1
    word=''.join(w)
    if ((word.count('3')==1) \
        and ((sum([1 for s in word if int(s)%2==0]))<=(sum([1 for s in word if int(s)%2!=0])))):
        c+=1
        print(k,c,word)


#f=open('17var16.txt')
#a=[int(x) for x in f]
#k=0
#maks=0
#minsum=10000000000000000000000000000000000000000000000000000
#for i in range(len(a)):
#    if a[i]>maks:
#        maks=a[i]
#for i in range(len(a)-2):
#    if (((a[i]%3==0) + (a[i+1]%3==0) + (a[i+2]%3==0))==0) and \
#       (a[i]**2+a[i+1]**2+a[i+2]**2)>maks:
#        k+=1
#        if (a[i]**2+a[i+1]**2+a[i+2]**2)<minsum:
#            minsum=(a[i]**2+a[i+1]**2+a[i+2]**2)
#print(k,minsum)




f=open('0910.12.txt')
for s in f:
    a=sorted[(int(x) for x in s.split())]
    a2=[x for x in a if a.count(x)==2]
    if and 
















        
