from turtle import *
tracer(0)
screensize(5000,5000)
r=1
for i in range(2):
    fd(10*r)
    rt(90)
    fd(20*r)
    rt(90)
up()
for i in range(1):
    fd(3)
    rt(90)
    fd(5)
    lt(90)
down()
for i in range(2):
    fd(70*r)
    rt(90)
    fd(80*r)
    rt(90)
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'green')
update()
