def f(x):
    return ((x%12==0) and (x%5==0))<=(x%a==0)
for a in range(1,1000):
    if all(f(x) for x in range(1,10000)):
        print(a)
