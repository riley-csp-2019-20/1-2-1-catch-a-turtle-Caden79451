# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
turtleshape = "turtle"
turtlesize = 1
turtlecolor = "Purple"

score = 0

#-----initialize turtle-----
Mole1 = trtl.Turtle(shape = turtleshape)
Mole1.color(turtlecolor)
Mole1.shapesize(turtlesize)
Mole1.speed(0)
 
keeper = trtl.Turtle(shape = turtleshape)
keeper.color(turtlecolor)
keeper.shapesize(turtlesize)
keeper.ht()

keeper.penup()
keeper.goto(-300, 300)
keeper.pendown()
keeper.write(score)

#-----game functions--------
def turtle_clicked(x,y):
    print("Mole1 got clicked")
    change_position()
    update_score()

def change_position():
    Mole1.penup()
    Mole1.ht()
    Mole1x = random.randint(-400, 400)
    Mole1y = random.randint(-300, 300)
    Mole1.goto(Mole1x, Mole1y)
    Mole1.st()

def update_score():
    global score
    score += 1
    print(score)

#-----events----------------

wn = trtl.Screen()

Mole1.onclick(turtle_clicked)

wn.mainloop()