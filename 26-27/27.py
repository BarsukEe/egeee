import math
#f=open('27_A_23766.txt')
#a1,a2=[],[]
#for i in f:
 #   x,y=map(float,i.replace(',','.').split())
  #  (a1,a2)[y>8].append([x,y]) #при истине записывается в a1, при лжи в a2, условие: y>8
#def centr(k):
 #   return min(k,key=lambda dot1: sum(math.dist(dot1,dot2) for dot2 in k))
#c1=centr(a1)
#c2=centr(a2)
#px=min(c1[0],c2[0])
#py=min(c1[1],c2[1])
#print(int(px*10000),int(py*10000))

f=open('27_B_23766.txt')
a1,a2,a3=[],[],[]
for i in f:
    x,y=map(float,i.replace(',','.').split())
    if y>10 and y<20: a1.append([x,y])
    elif y>20 and y<30 and x<18: a2.append([x,y])
    elif x>18 and x<25: a3.append([x,y])
def centr(k):
    return min(k,key=lambda dot1: sum(math.dist(dot1,dot2) for dot2 in k))
c1=centr(a1)
c2=centr(a2)
c3=centr(a3)
q1=math.dist(c1,c3)
r1=max(math.dist(c1,dot) for dot in a1)
r2=max(math.dist(c2,dot) for dot in a2)
r3=max(math.dist(c3,dot) for dot in a3)
q2=max(r1,r2,r3)
print(int(q1*10000),int(q2*10000))
