def f(x,y):
    return (x*y<a) or (y>=x) or (x>12)
for a in range(1,1000):
    if all(f(x,y)==1 for x in range(1,10000) for y in range(1,10000)):
        print(a)
        break
