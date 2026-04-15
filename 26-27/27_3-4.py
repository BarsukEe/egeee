from math import dist
a1,a2=[],[]
f=open('27_A_27637.txt')
for i in f:
    x,y=map(float,i.replace(',','.').split())
    (a1,a2)[y<11].append([x,y])
#def centr(cl):
#    for t in cl:
#        m=min(sum([dist(t,t2) for t2 in cl]))
#    return m
def centr(k):
    return min(k,key=lambda dot1: sum(dist(dot1,dot2) for dot2 in k))
#def centr(cl):
#   m=[]
  #  for p in cl:
    #    s=sum(dist(p,p1) for p1 in cl)
    #    m.append([s,p])
    #return min(m)[1]
#c1=centr(a1)
#c2=centr(a2)
#print(min(len(a1),len(a2)))
#t=(-1,1.3)
#s=dist(c1,(-1,1.3))+dist(c2,(-1,1.3))
#print(int(s*10000))


#k=open('27_B_27637.txt')
#a1,a2,a3=[],[],[]
#for i in k:
  #  x,y=map(float,i.replace(',','.').split())
  #  if x<24 and y<21: a1.append([x,y])
   # elif x>24: a2.append([x,y])
    #elif y>23: a3.append([x,y])
#def centr(k):
 #   return min(k,key=lambda dot1: sum(dist(dot1,dot2) for dot2 in k))
#t=[]
#c1=centr(a1)
#c2=centr(a2)
#c3=centr(a3)
#k1,k2,k3=0,0,0
#for i in a3:
 #   t.append(dist(c3,i))
#print((max(t)*10000))
#kk=0
#for i in a1:
 #   if dist(i,c1)<=1.6 and i!=c1:
 #       kk+=1
#print(kk) 
#    if dist(c1,(1,6))


#f=open('27A_20291.txt')
#a1,a2,a3,a4=[],[],[],[]
#for i in f:
#    x,y=map(float,i.split())
 #   if x>2 and y>2: a1.append([x,y])
  #  elif x>2 and y<2: a2.append([x,y])
  #  elif x<2 and y<0: a3.append([x,y])
  #  elif x<0 and y>0: a4.append([x,y])
#def centr(k):
 #   m = []
 #   for dot1 in k:
  #      d = max(dist(dot1,dot2) for dot2 in k)
  #      m.append(d)
 #   return max(m)
#d1=centr(a1)
#d2=centr(a2)
#d3=centr(a3)
#d4=centr(a4)
#print(min(d1,d2,d3,d4)*100000)
#print(((d1+d2+d3+d4)/4)*100000)

f=open('27B_20291.txt')
a1,a2,a3,a4,a5,a6,a7=[],[],[],[],[],[],[]
for i in f:
    x,y=map(float,i.split())
    if y>1 and x>0.9 and x<6.2: a1.append([x,y])
    elif x>6.2 and y>3: a2.append([x,y])
    elif x>1 and x<6 and y<1 and y>-4: a3.append([x,y])
    elif x>6 and y<0: a4.append([x,y])
    elif x<1 and x>-4 and y<3 and y>-2: a5.append([x,y])
    elif y<-4: a6.append([x,y])
    elif x<-4: a7.append([x,y])
def centr(k):
    m=[]
    for dot1 in k:
        d=max(dist(dot1,dot2) for dot2 in k)
        m.append(d)
    return max(m)
d1=centr(a1)
d2=centr(a2)
d3=centr(a3)
d4=centr(a4)
d5=centr(a5)
d6=centr(a6)
d7=centr(a7)
print(min(d1,d2,d3,d4,d5,d6,d7)*100000)
print(((d1+d2+d3+d4+d5+d6+d7)/7)*100000)









