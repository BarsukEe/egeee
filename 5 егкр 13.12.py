p=[]
def f(x,y):
    return (78125!=y+4*x) or (A>x) and (A>y)
#импликация (not(78125==y+4*x)) or (A>x) and (A>y)
#(78125=y+4*x)<=((A>x) and (A>y)
for y in range(1,100000):
    for x in range(1,100000):
        if y==78125-4*x:
            p.append([x,y])
for A in range(0,1000):
    if all(f(x,y)==1 for x,y in p):
        print(A)
#def tr(n):
 #   s=''
 #   while n>0:
 #       s=str(n%3)+s
#        n//=3
#    return s
#res=[]
#for n in range(1,100):
#    b=tr(n)
#    if n%3==0:
#        b+=b[-2:]
#    if n%3!=0:
        #b+=tr((b.count('1')+(b.count('2') * 2))*3)
        #или
        #b+=tr(sum([int(s) for s in f])*3)
        #или
        #b+=tr((sum(map(int,b)))*3)

  #  r=int(b,3)
 #   if r%2!=0 and r>208:
#        res.append(r)
#print(min(res))









        
    
