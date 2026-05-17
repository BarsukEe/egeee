#f=open("9_23747.txt")
#for s in f:
  #  a=[int(x) for x in s.split()]
  #  a1=[x for x in a if a.count(x)==3]
  #  anpv=[x for x in a if a.count(x)==1]
   # if len(a1)==3 and len(anpv)==4 and sum(anpv)/len(anpv)< a1[0]:
    #    print(sum(a))
        
    
#f=open("23555.txt")
#k=0
#for s in f:
#    a=[int(x) for x in s.split()]
#    a3=[x for x in a if a.count(x)==3]
#    a2=[x for x in a if a.count(x)==2]
#    anpv=[x for x in a if a.count(x)==1]
#    if len(a3) == 3 and len(a2)==2 and len(anpv)==2 and \
#       max(max(a2),max(a3))>max(anpv):
#        
 #       k+=1
#print(k)

#f=open("21895.txt")
#k=0
#for s in f:
 #   a=sorted([int(x) for x in s.split()])
  #  a1=[x for x in a if a.count(x)==1]
  #  if len(a1)==5 and (a[0]+a[1])<(a[2]+a[3]+a[4]):
  #      k+=1
#print(k)

f=open("21704.txt")
for s in f:
    a=sorted([int(x) for x in s.split()],reverse= True)
    am=sorted([int(x) for x in s.split()])
    if len(a)==7 and (am[0]+am[1])/len(a) > \
       (am[2]+am[3]+am[4]+am[5]+am[6])/len(a):
        print(sum(a))
