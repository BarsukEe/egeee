#from math import dist
#f=open('27_A.txt')
#cl=[[],[]]
#rg1=[]
#rg2=[]
#for s in f:
 #   x,y,z=[x for x in s.replace(',','.').split()]
 #   if float(x)<25:
  #      cl[0].append([float(x),float(y)])
    #    if 'III' in z and 'A' in z:
   #         rg1.append([float(x),float(y)])
  #  else:
  #      cl[1].append([float(x),float(y)])
   #     if 'III' in z and 'A' in z:
  #          rg2.append([float(x),float(y)])
#def centr(cl):
#    c=[]
#    for t in cl:
#        s=sum([dist(t,t1) for t1 in cl])     #центроид в файле с параметром (характеристикой звезды)
 #       c.append([s,t])
 #   return min(c)[1]

#for t in rg2:
#    m=dist(t,centr(cl[1]))
 #   print(m,int(10000*(t[0])))
 #   print(m,int(10000*(t[1])))

#f=open('27_B.txt')
#rg1=[]
#rg2=[]
#rg3=[]
#cl=[[],[],[]]
#for s in f:
#    x,y,z=[x for x in s.replace(',','.').split()]
 #   if float(y)<8:
  #      cl[0].append([float(x),float(y)])
  #      if 'V' in z and 'G' in z:
    #        rg1.append([float(x),float(y)])
    #elif float(y)>8 and float(y)<14:
     #   cl[1].append([float(x),float(y)])
      #  if 'V' in z and 'G' in z:
       #     rg2.append([float(x),float(y)])
    #elif float(y)>14 and float(y)<20:
    #    cl[2].append([float(x),float(y)])
     #   if 'V' in z and 'G' in z:
       #     rg3.append([float(x),float(y)])

#def centr(cl):
 #   s = []
  #  for t in cl:
   #     m=max([dist(t,t1) for t1 in cl])   #----для нахождения расстояния между двумя звёздами в кластере
   #     s.append(m)
   # return max(s)
#print(len(rg1),len(rg2),len(rg3))
#print(int(dist(centr(cl[0]),centr(cl[1]))*10000))
#60306
#print(rg1,rg2,rg3)
#print(int(10000*(centr(rg1))))
#print(int(10000*(centr(rg2))))
#print(int(10000*(centr(rg3))))
# а - 390205 182699
# б - 60306
