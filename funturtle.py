import turtle
#turtle.shape('turtle')
#square=turtle.clone()
#square.shape('square')
#square.goto(100,100)
#square.stamp()
#square.goto(100,150)
#square.stamp()
#square.goto(150,150)
#square.stamp()
#square.goto(150,100)
#square.stamp()
#square.goto(100,100)
#square.stamp()
#turtle.mainloop()

#turtle.shape('turtle')
#triangle=turtle.clone()
#triangle.shape('triangle')
#triangle.goto(100,100)
#triangle.stamp()
#triangle.goto(200,50)
#triangle.stamp()
#triangle.goto(50,50)
#triangle.stamp()
#turtle.mainloop()

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP
def up():
    global direction
    direction=UP
    print('you pressed up')
    return direction

def down():
    global direction
    direction=DOWN
    print('you perssed down')
    return direction

def left():
    global direction
    direction=LEFT
    print('you pressed left')
    return direrction

def right():
    global direction
    direction=RIGHT
    print('you pressed right')
    return directon

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)


