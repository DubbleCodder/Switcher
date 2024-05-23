import turtle
import random

def collide(a, b):
    return abs(a.xcor() - b.xcor()) < 30 and abs(a.ycor() - b.ycor()) < 30

def collideZ(a, b):
    return abs(a.xcor() - b.xcor()) < 1000 and abs(a.ycor() - b.ycor()) < 30

def gravity():
    y = plr.ycor()
    y -= 6
    plr.sety(y)



player = 'C:/Users/cassi/Music/pics/player.gif'
island = 'C:/Users/cassi/Music/pics/island.gif'
bad = 'C:/Users/cassi/Music/pics/bad.gif'

sc = turtle.Screen()
sc.setup(1280, 720)
sc.bgcolor('light blue')
sc.addshape(player)
sc.addshape(island)
sc.addshape(bad)

plr = turtle.Turtle()
plr.shape(player)
plr.penup()
plr.speed(99999999999999999999999999999999)
plr.goto(0, 0)

floor = turtle.Turtle()
floor.shape(island)
floor.penup()
floor.speed(9999999999999999999999999999999999)
floor.goto(0, 0)

floor2 = turtle.Turtle()
floor2.shape(island)
floor2.penup()
floor2.speed(9999999999999999999999999999999999)
floor2.goto(30, 30)

floor3 = turtle.Turtle()
floor3.shape(island)
floor3.penup()
floor3.speed(9999999999999999999999999999999999)
floor3.goto(30, 30)

floor4 = turtle.Turtle()
floor4.shape(island)
floor4.penup()
floor4.speed(9999999999999999999999999999999999)
floor4.goto(30, 30)

kill = turtle.Turtle()
kill.shape(bad)
kill.penup()
kill.speed(900000000000000000)
kill.goto(100, 100)

die = turtle.Turtle()
die.shape("square")
die.turtlesize(1, 1000)
die.color('light blue')
die.penup()
die.speed(99999999999999999999999999999999999999)
die.goto(0, -280)

def switch():
    x = random.randint(-420, 420)
    y = random.randint(-420, 420)

    floor.goto(x, y)

    sc.ontimer(switch, 6000)

def switch2():
    x = random.randint(-420, 420)
    y = random.randint(-420, 420)

    floor2.goto(x, y)

    sc.ontimer(switch2, 6000)

def switch3():
    x = random.randint(-420, 420)
    y = random.randint(-420, 420)

    floor3.goto(x, y)

    sc.ontimer(switch3, 6000)

def switch4():
    x = random.randint(-420, 420)
    y = random.randint(-420, 420)

    floor4.goto(x, y)

    sc.ontimer(switch4, 6000)

def kill_act():
    x = random.randint(-420, 420)
    y = random.randint(-420, 420)

    kill.goto(x, y)

    sc.ontimer(kill_act, 4000)

kill_act()

switch4()
switch3()
switch2()
switch()

def a():
    x = plr.xcor()
    x -= 10
    plr.setx(x)

def d():
    x = plr.xcor()
    x += 10
    plr.setx(x)

def space():
    y = plr.ycor()
    y += 90
    plr.sety(y)

turtle.listen()
turtle.onkeypress(a, 'a')
turtle.onkeypress(d, 'd')
turtle.onkeypress(space, 'space')

while True:
    sc.update()

    gravity()

    if collide(plr, floor):
        y = plr.ycor()
        y += 12
        plr.sety(y)

    if collideZ(plr, die):
        turtle.bye()

    if collide(plr, floor2):
        y = plr.ycor()
        y += 12
        plr.sety(y)

    if collide(plr, floor3):
        y = plr.ycor()
        y += 12
        plr.sety(y)

    if collide(plr, floor4):
        y = plr.ycor()
        y += 12
        plr.sety(y)

    if collide(plr, kill):
        turtle.bye()

    








