#PythonDraw.py

'''导入turtlr包'''
import turtle

turtle.setup(600,350)
turtle.pu()
turtle.fd(-200)
turtle.pd()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()