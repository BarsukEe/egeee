f=open('26_9847.txt')
n=int(f.readline())
a=[0]*24*60
for i in range(n):
    x,y=map(int,f.readline().split())
    for j in range(x,y):
        a[j]+=1
m=max(a)
for i in range(len(a)):
    if a[i]==m:
        print(i)
#ответ- 2 пика и m
