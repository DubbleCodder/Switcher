import turtle
import random

def collide(a, b):
    return abs(a.xcor() - b.xcor()) < 30 and abs(a.ycor() - b.ycor()) < 30

def collideZ(a, b):
    return abs(a.xcor() - b.xcor()) < 1000 and abs(a.ycor() - b.ycor()) < 30

def collide2(a, b):
    return abs(a.xcor() - b.xcor()) < 30 and abs(a.ycor() - b.ycor()) < 5000

player = 'C:/Users/cassi/Music/pics/player.gif'
player2 = 'C:/Users/cassi/Music/pics/player2.gif'
player3 = 'C:/Users/cassi/Music/pics/player3.gif'
island = 'C:/Users/cassi/Music/pics/island.gif'
island2 = 'C:/Users/cassi/Music/pics/island2.gif'
bad = 'C:/Users/cassi/Music/pics/bad.gif'
cloud = 'C:/Users/cassi/Music/pics/cloud.gif'
island3 = 'C:/Users/cassi/Music/pics/desisland.gif'
island4 = 'C:/Users/cassi/Music/pics/desisland2.gif'

sc = turtle.Screen()
sc.setup(1280, 720)
sc.bgcolor('light blue')
sc.addshape(player)
sc.addshape(island)
sc.addshape(bad)
sc.addshape(island2)
sc.addshape(cloud)
sc.addshape(island3)
sc.addshape(island4)

plr = turtle.Turtle()
plr.shape(player)
plr.penup()
plr.speed(99999999999999999999999999999999)
plr.goto(0, 0)

def gravity():
    y = plr.ycor()
    y -= 8
    plr.sety(y)

islandtype = [1, 2]
itype = random.choice(islandtype)

islandtype2 = [1, 2]
itype2 = random.choice(islandtype2)

islandtype3 = [1, 2]
itype3 = random.choice(islandtype3)

islandtype4 = [1, 2]
itype4 = random.choice(islandtype4)

if itype == 1:
    floor = turtle.Turtle()
    floor.shape(island)
    floor.penup()
    floor.speed(9999999999999999999999999999999999)
    floor.goto(0, 0)
    
elif itype == 2:
    floor = turtle.Turtle()
    floor.shape(island3)
    floor.penup()
    floor.speed(9999999999999999999999999999999999)
    floor.goto(0, 0)

if itype2 == 1:
    floor2 = turtle.Turtle()
    floor2.shape(island)
    floor2.penup()
    floor2.speed(9999999999999999999999999999999999)
    floor2.goto(30, 30)
elif itype2 == 2:
    floor2 = turtle.Turtle()
    floor2.shape(island3)
    floor2.penup()
    floor2.speed(9999999999999999999999999999999999)
    floor2.goto(30, 30)

if itype3 == 1:
    floor3 = turtle.Turtle()
    floor3.shape(island)
    floor3.penup()
    floor3.speed(9999999999999999999999999999999999)
    floor3.goto(30, 30)
elif itype3 == 2:
    floor3 = turtle.Turtle()
    floor3.shape(island3)
    floor3.penup()
    floor3.speed(9999999999999999999999999999999999)
    floor3.goto(30, 30)

if itype4 == 1:
    floor4 = turtle.Turtle()
    floor4.shape(island)
    floor4.penup()
    floor4.speed(9999999999999999999999999999999999)
    floor4.goto(30, 30)
elif itype4 == 2:
    floor4 = turtle.Turtle()
    floor4.shape(island3)
    floor4.penup()
    floor4.speed(9999999999999999999999999999999999)
    floor4.goto(30, 30)

kill = turtle.Turtle()
kill.shape(bad)
kill.penup()
kill.speed(900000000000000000)
kill.goto(100, 100)

cld = turtle.Turtle()
cld.shape(cloud)
cld.penup()
cld.speed(9999999999999999999999999)
cld.goto(500, 320)

cld2 = turtle.Turtle()
cld2.shape(cloud)
cld2.penup()
cld2.speed(9999999999999999999999999)
cld2.goto(500, 220)

cld3 = turtle.Turtle()
cld3.shape(cloud)
cld3.penup()
cld3.speed(9999999999999999999999999)
cld3.goto(500, -190)

cld4 = turtle.Turtle()
cld4.shape(cloud)
cld4.penup()
cld4.speed(9999999999999999999999999)
cld4.goto(500, -320)

cle = turtle.Turtle()
cle.shape('square')
cle.color('blue')
cle.turtlesize(100, 1)
cle.penup()
cle.speed(9999999999999999999999999999999999999999999999)
cle.goto(-700, 0)

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

def frames():
    if floor.shape() == island:
        floor.shape(island2)
    elif floor.shape() == island2:
        floor.shape(island)

    if floor2.shape() == island:
        floor2.shape(island2)
    elif floor2.shape() == island2:
        floor2.shape(island)

    if floor3.shape() == island:
        floor3.shape(island2)
    elif floor3.shape() == island2:
        floor3.shape(island)

    if floor4.shape() == island:
        floor4.shape(island2)
    elif floor4.shape() == island2:
        floor4.shape(island)

    if floor.shape() == island3:
        floor.shape(island4)
    elif floor.shape() == island4:
        floor.shape(island3)

    if floor2.shape() == island3:
        floor2.shape(island4)
    elif floor2.shape() == island4:
        floor2.shape(island3)

    if floor3.shape() == island3:
        floor3.shape(island4)
    elif floor3.shape() == island4:
        floor3.shape(island3)

    if floor4.shape() == island3:
        floor4.shape(island4)
    elif floor4.shape() == island4:
        floor4.shape(island3)

    sc.ontimer(frames, 200)

def cloud_move():
    x = cld.xcor()
    x -= 12
    cld.setx(x)

    x = cld2.xcor()
    x -= 10
    cld2.setx(x)

    x = cld3.xcor()
    x -= 9
    cld3.setx(x)

    x = cld4.xcor()
    x -= 13
    cld4.setx(x)

    sc.ontimer(cloud_move, 40)

cloud_move()

frames()

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

    if collide2(cld, cle):
        cld.goto(500, 320)

    if collide2(cld2, cle):
        cld2.goto(500, 220)

    if collide2(cld3, cle):
        cld3.goto(500, -190)

    if collide2(cld4, cle):
        cld4.goto(500, -320)

    








