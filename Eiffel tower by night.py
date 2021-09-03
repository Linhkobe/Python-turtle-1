
import turtle
import random
from random import randint
screen = turtle.Screen()
screen.setup(1000,1000)
screen.bgcolor("navy")
screen.title("Project 1: La tour eiffel")
##
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed(0)
circle.up()
circle.goto(0,350)

square1 = turtle.Turtle()
square1.shape('square')
square1.color('white')
square1.speed(0)
square1.up()
square1.goto(0,320)

square2 = turtle.Turtle()
square2.shape('square')
square2.color('white')
square2.speed('fastest')
square2.up()
square2.goto(0,287)
# 1st rectangle :   
square = turtle.Turtle()
square.shape('square')
square.color('white')
square.speed(0)
square.up()
##
tower = turtle.Turtle()
tower.shape('square')
tower.color('blue')
tower.speed(0)
tower.up()
##
leg1 = turtle.Turtle()
leg1.shape('square')
leg1.color('red')
leg1.speed(0)
leg1.up()

leg2 = turtle.Turtle()
leg2.shape('square')
leg2.color('red')
leg2.speed(0)
leg2.up()

leg3 = turtle.Turtle()
leg3.shape('square')
leg3.color('red')
leg3.speed(0)
leg3.up()

leg4 = turtle.Turtle()
leg4.shape('square')
leg4.color('red')
leg4.speed(0)
leg4.up()
# 2nd rectangle :
square3 = turtle.Turtle()
square3.shape('square')
square3.color('white')
square3.speed(0)
square3.up()
square3.goto(0,250)
# 2nd rectangle :
square4 = turtle.Turtle()
square4.shape('square')
square4.color('blue')
square4.speed(0)
square4.up()
square4.goto(0,40)
# Part 2: 5 squares on the right:
square5 = turtle.Turtle()
square5.shape('square')
square5.color('blue')
square5.speed(0)
square5.up()
square5.goto(90,-60)

square6 = turtle.Turtle()
square6.shape('square')
square6.color('blue')
square6.speed(0)
square6.up()
square6.goto(90,-90)

square7 = turtle.Turtle()
square7.shape('square')
square7.color('blue')
square7.speed(0)
square7.up()
square7.goto(90,-120)

square8 = turtle.Turtle()
square8.shape('square')
square8.color('blue')
square8.speed('fastest')
square8.up()
square8.goto(120,-90)

square9 = turtle.Turtle()
square9.shape('square')
square9.color('blue')
square9.speed(0)
square9.up()
square9.goto(120,-120)
# Part 2: 2 squares on the left:
square10 = turtle.Turtle()
square10.shape('square')
square10.color('blue')
square10.speed(0)
square10.up()
square10.goto(-90,-60)

square11 = turtle.Turtle()
square11.shape('square')
square11.color('blue')
square11.speed(0)
square11.up()
square11.goto(-90,-90)

square12 = turtle.Turtle()
square12.shape('square')
square12.color('blue')
square12.speed(0)
square12.up()
square12.goto(-90,-120)

square13 = turtle.Turtle()
square13.shape('square')
square13.color('blue')
square13.speed(0)
square13.up()
square13.goto(-120,-90)

square13 = turtle.Turtle()
square13.shape('square')
square13.color('blue')
square13.speed(0)
square13.up()
square13.goto(-120,-120)
# 1st rectangle:
for i in range(1,3):
    y = 30*i
    for j in range(3):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
# Big column:
for i in range(1,8):
    y = 30*i
    for j in range(2):
        x = 30*j
        square3.goto(x,-y+250)
        square3.stamp()
        square3.goto(x,-y+250)
        square3.stamp()
        square3.goto(-x,-y+250)
        square3.stamp()
# 2nd rectangle:        
for i in range(1,3):
    y = 30*i
    for j in range(4):
        x = 30*j
        square4.goto(x,-y+40)
        square4.stamp()
        square4.goto(x,-y+40)
        square4.stamp()
        square4.goto(-x,-y+40)
        square4.stamp()
        
# 3rd rectangle:
for i in range(1,3):
    y = 30*i
    for j in range(6):
        x = 30*j
        tower.goto(x,-y-120)
        tower.stamp()
        tower.goto(x,-y-120)
        tower.stamp()
        tower.goto(-x,-y-120)
        tower.stamp()

# Leg1 :
for i in range(1,3):
    y = 30*i
    for j in range(3):
        x = 30*j
        leg1.goto(-x-150,-y-190)
        leg1.stamp()
        leg1.goto(-x-150,-y-190)
        leg1.stamp()

# Leg2 :
for i in range(1,3):
    y = 30*i
    for j in range(3):
        x = 30*j
        leg2.goto(-x+210,y-280)
        leg2.stamp()
        leg2.goto(-x+210,y-280)
        leg2.stamp()

# Leg3 :
for i in range(1,3):
    y = 30*i
    for j in range(3):
        x = 30*j
        leg3.goto(-x+250,-y-250)
        leg3.stamp()
        leg3.goto(-x+250,-y-250)
        leg3.stamp()

# Leg4 :
for i in range(1,3):
    y = 30*i
    for j in range(3):
        x = 30*j
        leg4.goto(-x-190,y-340)
        leg4.stamp()
        leg4.goto(-x-190,y-340)
        leg4.stamp()

colors = ["red","blue","orange","yellow","magenta","teal","peru","ivory","crimson","deeppink"]

moon = turtle.Turtle()
moon.hideturtle()
moon.speed(7)

star = turtle.Turtle()
star.hideturtle()
star.speed(0)

def draw_moon(pos,color): # position and color of the moon
    x,y = pos
    moon.color(color)
    moon.begin_fill()
    moon.penup()
    moon.goto(x,y)
    moon.pendown()
    moon.circle(50)
    moon.end_fill()

draw_moon((-300,170),"gold")
draw_moon((-278,183),"navy")

def draw_star(pos,color,length): # position, color and length(size) of star
    x,y = pos
    star.color(color)
    star.penup()
    star.goto(x,y)
    star.pendown()
    star.begin_fill()
    for i in range(5):
        star.forward(length)
        star.right(144)
        star.forward(length)
##        star.forward(length)
##        star.left(90)
    star.end_fill()

draw_star((100,100),"red",10)

def random_pos():
    return (random.randint(-390,390),random.randint(-200,290))

def random_length():
    return random.randint(5,25)


for i in range(30):
    color = random.choice(colors)
    pos = random_pos()
    length = random_length()

    draw_star(pos,color,length)

    
    

"""
for n in range(50):
    linh.forward(100)
    linh.left(40)
    linh.forward(100)
    linh.left(90)
    linh.forward(100)
    linh.left(90)
    linh.forward(100)
    linh.left(40)
"""
"""
for n in range(30):
    linh.forward(50)
    linh.left(90)
    linh.forward(100)
    linh.left(45)
    linh.forward(100)
    linh.left(90)
    linh.forward(50)
    linh.left(40)
    
linh.end_fill()
turtle.done()
"""
"""
l.penup()
l.goto(0,300)
l.pendown()
for i in range(4):
    l.forward(50)
    l.right(90)
    for k in range(i):
        l.penup()
        l.forward(100)
        l.pendown()
        l.forward(50)
        l.right(90)
    
        
l.end_fill()
"""

