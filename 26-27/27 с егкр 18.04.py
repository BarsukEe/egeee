from math import dist
a1,a2=[],[]
k=0
f=open('27_A_28946.txt')
def centr(k):
    return min(k,key=lambda dot1: sum(dist(dot1,dot2) for dot2 in k))
for i in f:
    x,y=map(float,i.replace(',','.').split())
    (a1,a2)[y<15].append([x,y])
c1=centr(a1)
c2=centr(a2)
for t in a1:
    if t[1]<c1[1]:
        k+=1
print(k)
print(abs(int(10000*(c1[0]-c2[0]))))



##f=open('27_B_28946.txt')
##k=0
##a1,a2,a3=[],[],[]
##for i in f:
##    x,y=map(float,i.replace(',','.').split())
##    if x<24 and x>16 and y<21: a1.append([x,y])
##    elif x>24: a2.append([x,y])
##    elif y>21: a3.append([x,y])
##def centr(k):
##    return min(k,key=lambda dot1: sum(dist(dot1,dot2) for dot2 in k))
##c1=centr(a1)
##c2=centr(a2)
##c3=centr(a3)
##
##k=sum([1 for t in a2 if abs(c2[0]-t[0])<=0.9 and abs(c2[1]-t[1])<=0.9])
##print(k)
