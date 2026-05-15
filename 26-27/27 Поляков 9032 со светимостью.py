from math import dist
##f=open('27AA.txt')
##a1,a2=[],[]
##bz1=[]
##bz2=[]
##for i in f:
##    x,y,z=[x for x in i.replace(',','.').split()]
##    if float(y)<8:
##        a1.append([float(x),float(y)])
##        if 'L' in z and '3' in z: bz1.append([float(x),float(y)])
##    elif float(y)>8:
##        a2.append([float(x),float(y)])
##        if 'L' in z and '3' in z: bz2.append([float(x),float(y)])
##def centr(k):
##    return min(k,key=lambda dot1: sum(dist(dot1,dot2) for dot2 in k))
##c1=centr(a1)
##c2=centr(a2)
##r1=[]
##r2=[]
###131 92
##r1=int(10000*dist(c2,bz2[0]))
##r2=[]
##for t in bz1:
##    r2.append(int(10000*dist(t,c2)))
##print(max(r2),r1)
##r4=int(10000*dist(c1,bz2[0]))
##r3=[]
##for t in bz1:
##    r3.append(int(10000*dist(t,c1)))
##print(max(r3),r4)

f=open('27BB.txt')
a1,a2,a3=[],[],[]
bz1,bz2,bz3=[],[],[]
for i in f:
    x,y,z=[x for x in i.replace(',','.').split()]
    if float(x)>20:
        a1.append([float(x),float(y)])
        if 'L' in z: bz1.append([float(x),float(y)])
    elif float(y)<22 and float(x)>10 and float(x)<20:
        a2.append([float(x),float(y)])
        if 'L' in z: bz2.append([float(x),float(y)])
    elif float(y)>23:
        a3.append([float(x),float(y)])
        if 'L' in z: bz3.append([float(x),float(y)])
def centr(k):
    return min(k,key=lambda dot1: sum(dist(dot1,dot2) for dot2 in k))
c1=centr(a1)
c2=centr(a2)
c3=centr(a3)
#print(len(bz1),len(bz2),len(bz3))
#77 14 8
#print(int(10000*dist(c1,c3)))
r=[]
for t in bz1:
    for t1 in bz2:
        r.append(int(10000*dist(t,t1)))
for t in bz1:
    for t1 in bz3:
        r.append(int(10000*dist(t,t1)))
for t in bz2:
    for t1 in bz3:
        r.append(int(10000*dist(t,t1)))
print(max(r))





    
    
