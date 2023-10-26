import turtle 
import random

t = turtle.Turtle()
t2 = turtle.Turtle()
t2.setposition(-1,0)
#turtle.Screen().bgcolor("black")
t.speed(0)
t2.speed(0)
turtle.colormode(255)

def outerCircles(t,radius,numCircles,numRings):
  for i in range(numCircles):
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    t.pencolor(a,b,c)
    for j in range(numRings):
      t.circle(radius)
      radius = radius-5
    t.right(360/numCircles)
    radius = radius + (5*numRings)

# outerCircles(t,100,10,10)
# outerCircles(t,200,10,15)
# outerCircles(t,300,20,15)

def growVoid(t,radius):
  t2.right(90)
  a=255
  for i in range(radius):
    t.color(a,a,a)
    t2.goto(-51+i,0)
    t2.begin_fill()
    t2.circle(51-(i))
    t2.end_fill()
    t2.penup()
    #t2.goto(-51+i,0)
    t2.pendown()
    a=a-5

growVoid(t2,51)
outerCircles(t,100,10,10)
outerCircles(t,200,10,15)
outerCircles(t,300,20,15)
t.hideturtle()
t2.hideturtle()