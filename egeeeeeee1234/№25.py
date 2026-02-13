#n=36
#d=set()
#for i in range(1,int(n**0.5)+1):
#    if n%i==0:
#        d.add(i)
#        d.add(n//i)
#print(*d)


#def dl(x):
 #   d=set()
  #  for i in range(2,int(x**0.5)+1):
   #     if x%i==0:
    #        d.add(i)
     #       d.add(x//i)
#    return sorted(d)
#for x in range(81234,134690):
#    if len(dl(x))==3:
#        print(x,dl(x))

#def dl(x):
#    d=set()
#    for i in range(2,int(x**0.5)+1):
#        if x%i==0:
#            d.add(i)
#            d.add(x//i)
#    return sorted(d)
#for x in range(135790,163229):
 #   if sum(dl(x))>460000:
 #       print(len(dl(x)),sum(dl(x)))

#kub=[x**3 for x in range(1,1000) if x%2!=0]
#def dl(x):
   # d=set()
 #   for i in range(1,int(x**0.5)+1):
     #   if x%i==0:
       #     if i!=1: d.add(i)
         #   d.add(x//i)
    #return sorted(d)
#for x in range(228224,531136):
  #  b=[]
    #a=dl(x)
    #for i in a:
      #  if i in kub:
        #    b.append(i)
    #if len(b)>=4:
      #  print(len(b),max(b))
            




#25.8
#def pr(x):
  #  return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
#
#def dl(x):
  #  d=set()
    #for i in range(2,int(x**0.5)+1):
      #  if  x%i==0:
        #    d.add(i)
          #  d.add(x//i)
    #return sorted(d)
#for x in range(25317,51238):
  #  a=dl(x)
    #b=[]
    #for i in a:
      #  if pr(i):
        #    b.append(i)
    #if len(b)>=6:
      #  print(max(b),x)


#25.12
#k=0
#def pr(x):
#    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
#for x in range(6638225,6638323):
  #  if pr(x):
    #    k+=1
      #  print(k,x)





#25.13
#k=0
#for x in range(33333,55556):
  #  a=str(x)
    #if int(a[0])%2!=0 and int(a[1])%2!=0:
      #  if x%7==0 and x%11==0 and x%13==0:
        #    k+=1
          #  print(k,x)

#25.14

#def pr(x):
  #  return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))

#def dl(x):
  #  d=set()
    #for i in range(2,int(x**0.5)+1):
      #  if x%i==0:
        #    d.add(i)
          #  d.add(x//i)
    #return sorted(d)


#for x in range(33333,55555):
  #  a=dl(x)
    #b=[]
    #for i in a:
      #  if pr(i):
        #    b.append(i)
    #if len(b)!=0:
      #  if x%sum(b)==0:
        #    if sum(b)>250:
          #      print(i,sum(b))
    


def p(x):
    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
for x in range(33333,55555):
    if p(x):
        s=str(x)
        if int(s[0])+int(s[1])+int(s[2])+int(s[3])+int(s[4])>35:
            print(s,int(s[0])+int(s[1])+int(s[2])+int(s[3])+int(s[4]))





















