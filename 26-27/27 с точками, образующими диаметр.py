from math import dist
##a1,a2=[],[]
##f=open('27A_27591.txt')
##for i in f:
##    x,y=map(float,i.replace(',','.').split())
##    (a1,a2)[y<8].append([x,y])
##def c(k):
##    c=[]
##    for t in k:
##        for t1 in k:                            #ф-ция для нахождения точек, образующих диаметр
##            d=dist(t,t1)
##            c.append([d,t,t1])
##    return max(c)[1:]
##d1=c(a1)
##d2=c(a2)
##print(int(10000*(d2[0][0]+d2[1][0])))
##print(int(10000*(d1[0][1]+d1[1][1])))
##print(int(10000*(d2[0][1]+d2[1][1])))


f=open('27B_27591.txt')
a1,a2,a3=[],[],[]
for i in f:
    x,y=map(float,i.replace(',','.').split())
    if y<19 and x>6 and x<15: a1.append([x,y])
    elif x>9 and x<18 and y<27 and y>20: a2.append([x,y])
    elif x>18 and x<26 and y<28 and y>21: a3.append([x,y])
def c(k):
    c=[]
    for t in k:
        for t1 in k:
            d=dist(t,t1)
            c.append([d,t,t1])
    return max(c)[1:]
d1=c(a1)
d2=c(a2)
d3=c(a3)
print(d3[1])
print(int(10000*(dist(d1[1],d3[0]))))










