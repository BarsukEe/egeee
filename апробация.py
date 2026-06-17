from itertools import *
#s='36 456 145 236 23 124'.split()
#v='AF AD AC FE DB CE CB BE'.split()
#print(*range(1,7))
#for p in permutations('ABCDEF'):
 #   if all(str(p.index(b)+1) in s[p.index(a)] for a,b in v):
  #      print(*p)

#def f(x,y,w,z):
  #  return ((not(z)) and y and x and (not(w))) or ((not(z)) and y and (not(x)) and (not(w))) or (z and y and x and (not(w)))
#for i in product([0,1],repeat=7):
  #  t=[(i[0],1,i[1],i[2]),(i[3],0,1,i[4]),(0,i[5],0,i[6])]
    #if len(t)==len(set(t)):
      #  for p in permutations('xywz'):
        #    if [f(**dict(zip(p,r))) for r in t]==[1,1,1]:
          #      print(p)


#for n in range(1,1000):
  #  b=bin(n)[2:]
    #if n%3==0:
      #  b+=b[-3:]
    #else:
      #  b+=bin(3*(n%3))[2:]
    #r=int(b,2)
    #if r<130:
     #   print(n,b,r)

#k=0
#c=0
#for word in product('ИРСТУЦ',repeat=5):
 #   k+=1
 #   w=''.join(word)
 #   if w[0]!='0' and w.count('И')==2 and w.count('ЦЦ')==0:
  #      c+=1
    #    print(k,c,w)

#from ipaddress import *
#k=0
#net=ip_network(f'172.16.96.0/255.255.224.0',0)
#for ip in net:
 #   if f'{ip:b}'.count('1')%2==0:
 #       k+=1
#print(k)

#def f(a,b,m):
  #  if a+b>=211: return m%2==0
    #if m==0: return 0
    #h=[f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
    #return any(h) if m%2!=0 else any(h)
#print('19',[b for b in range(1,194) if not f(17,b,1) and f(17,b,2)])
#print('20',[b for b in range(1,194) if not f(17,b,1) and not f(17,b,2) and f(17,b,3)])
#print('21',[b for b in range(1,194) if not f(17,b,1) and not f(17,b,2) and not f(17,b,3) and f(17,b,4)])



#def f(c,e):
  #  if c<e: return 0
    #if c==e: return 1
    #return f(c-1,e)+f(c//2,e)
#print(f(40,17)*f(17,6))

#from fnmatch import *
#for i in range(1,10**8,171):
  #  if fnmatch(str(i),'1*23??56'):
    #    print(i,i//171)

#a=[int(x) for x in open('17_27629.txt')]
#b=[]
#maks=-100000
#for i in range(len(a)):
  #  if 999<abs(a[i])<10000 and a[i]>maks and abs(a[i])%100==43:
    #    maks=a[i]
#for i in range(len(a)-1):
  #  if ((999<abs(a[i])<10000)+(999<abs(a[i+1])<10000)>=1) and (a[i]+a[i+1])**2<maks**2:
    #    b.append((a[i]+a[i+1])**2)
#print(len(b),max(b))



#from functools import *
#@lru_cache(None)
#def f(n):
  #  if n==1: return 1
    #if n>1: return n*f(n-1)
#for n in range(1,1000000):
  #  f(n)
#print((f(2024)-5*f(2023))//f(2022))


#def f(x):
  #  return (x%25==0)<=((x%a!=0)<=(x%60!=0))
#for a in range(1,10000):
  #  if all(f(x)==1 for x in range(1,100000)):
    #    print(a)

#command={
  #  (' ',0):(' ',-1,1),
    #(' ',1):(' ',1,2),
    #(' ',3):(' ',1,4),
#    (' ',4):(' ',3,4),
  #  ('0',1):('0',-1,1),
    #('0',2):('0',1,2),
#    ('0',3):('0',1,3),
  #  ('0',4):('0',1,4),
    #('1',1):('1',-1,1),
#    ('1',2):('1',1,3),
  #  ('1',3):('0',1,4),
    #('1',4):('1',1,4)
#}
#def mt(s):
   # s=list(' '+s+' ')
    #q=0
    #i=len(s)-1
   # while True:
      #  cmd=command[(s[i],q)]
        #s[i]=cmd[0]
        #if cmd[1]==3: break
        #i+=cmd[1]
      #  q=cmd[2]
    #return ' '.join(s)
#print(int(mt('1100100000'),2))



for x in range(1,2031):
    a=6**100+6**2030-x
    b = ''
    while a>0:
        b=str(a%6)+b
        a//=6
print(b.count('0'))

