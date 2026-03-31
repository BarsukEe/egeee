f=open('26_23765.txt')
n=int(f.readline())
a=[]
for i in range(n):
    x,y = map(int,f.readline().split())
    a.append([i+1,x,y,min(x,y)])
print(max(a,key=lambda x:x[-1]))
print(sum(1 for i in a if i[1]>i[2])-1)
