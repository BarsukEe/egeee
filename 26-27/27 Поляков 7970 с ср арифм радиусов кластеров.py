from math import dist
##f=open('27A.txt')
##a1,a2=[],[]
##A=(4,0)
##B=(10,11)
##k=11/6
##b=0-k*4
##for i in f:
##    x,y=map(float,i.replace(',','.').split())
##    (a1,a2)[y<k*x+b].append([x,y])
##def centr(k):
##    return min(k,key=lambda dot1: sum(dist(dot1,dot2) for dot2 in k))
##c1=centr(a1)
##c2=centr(a2)
##r1=max([dist(t,c1) for t in a1])
##r2=max([dist(t,c2) for t in a2])
##print(int(10000*((r1+r2)/2)))
A=(2.9,3.7)
B=(7.5,8.5)
k=4.8/4.6
b=3.7-k*2.9
f=open('27B.txt')
a1,a2,a3,a4=[],[],[],[]
def centr(k):
    return min(k,key=lambda dot1: sum(dist(dot1,dot2) for dot2 in k))

for i in f:
    x,y=map(float,i.replace(',','.').split())
    if x<2.2 and y<6.8: a1.append([x,y])
    elif y<2.6 and x<5.2: a2.append([x,y])
    elif y<k*x+b: a3.append([x,y])
    elif y>k*x+b: a4.append([x,y])
c1=centr(a1)
c2=centr(a2)
c3=centr(a3)
c4=centr(a4)
r1=max([dist(t1,c1) for t1 in a1])
r2=max([dist(t1,c2) for t1 in a2])
r3=max([dist(t1,c3) for t1 in a3])
r4=max([dist(t1,c4) for t1 in a4])
print(int(10000*((r1+r2+r3+r4)/4)))























