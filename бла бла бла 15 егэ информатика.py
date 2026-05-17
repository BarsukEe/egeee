#from itertools import *
#def f(x):
  #  p=43<=x<=49
  #  q=44<=x<=53
 #   a=a1<=x<=a2
 #   return (a<=p) or q
#ox=[i/4 for i in range(42*4,54*4)]
#m=[]
#for a1,a2 in combinations(ox,2):
#    if all(f(x)==1 for x in ox):
#        m.append(a2-a1)
#print(max(m))



#def f(x):
   # return (x%128==0)<=(x%a!=0)<=(x%80!=0)
#for a in range(1,1000):         
 #   if all(f(x)==1 for x in range(1,10000)):
  #      print(a)
        
def f(x):
    return (x%a==0) or ((x%b==0)<=(x%22!=0))
for a in range(1,1000):
    if all(f(x) for x in range(1,10000)):
           print(a)


                #15 егэ битовые цепочки
#from itertools import *
#bit=[''.join(i) for i in product('01',repeat=8)]
#a=set()
#p={i for i in bit if i[0]+i[1]=='11'}
#q={i for i in bit if i[-1]=='0'}
#def f(x):
 #   A=x in a
 #   P=x in p
#    Q=x in q
 #   return (not A)<=((not P) or Q)
#for x in bit:
 #   if f(x)==0:
 #       a.add(x)

#print(len(a))
