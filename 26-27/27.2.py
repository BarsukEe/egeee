import math
#f=open('27A_18678.txt')
#a1,a2=[],[]
#for i in f:
   # x,y=map(float,i.replace(',','.').split())
  #  if y<2: a1.append([x,y])
 #   elif x>1 and x<6: a2.append([x,y])
#def centr(k):
 #   return min(k,key=lambda dot1:sum(math.dist(dot1,dot2) for dot2 in k))
#c1=centr(a1)
#c2=centr(a2)
#px=(c1[0]+c2[0])/2*100000
#py=(c1[1]+c2[1])/2*100000
#print(int(px),int(py))
f=open('27B_18678.txt')
a1,a2,a3=[],[],[]
A=(1.0,9.0)
B=(5.0,-1.0)
k=(-1-9)/(5-1)
b=9-k*1
for i in f:
    x,y=map(float,i.replace(',','.').split())
    if y>9 and y<11 and x>8.5 and x<10: pass
    elif y<k*x+b and y>-1 and y<8.1: a1.append([x,y])
    elif x<6.2 and y<7 and y>1.5:a2.append([x,y])
    elif y>-1.7 and y<10.2 and x>4.6 and x<10:a3.append([x,y])
def centr(k):
    return min(k,key=lambda dot1:sum(math.dist(dot1,dot2) for dot2 in k))
c1=centr(a1)
c2=centr(a2)
c3=centr(a3)
px=(c1[0]+c2[0]+c3[0])/3*100000
py=(c1[1]+c2[1]+c3[1])/3*100000
print(int(px),int(py))
