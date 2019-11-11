import turtle

def draw1(mult=1, position=None):
    #   Draws a number then takes the multiplier to size it.
    #   Height = 50
    #   Width = 60
    origpos = turtle.pos()
    if position:
        turtle.setpos(position)
    turtle.setheading(0)
    turtle.pd()
    turtle.right(90)
    turtle.forward(50*mult)
    turtle.right(90)
    turtle.forward(20*mult)
    turtle.left(180)
    turtle.forward(40*mult)
    turtle.left(180)
    turtle.pu()
    turtle.forward(20*mult)
    turtle.right(90)
    turtle.forward(50*mult)
    turtle.left(150)
    turtle.pd()
    turtle.forward(20*mult)
    turtle.pu()
    return origpos

def draw4(mult=1, position=None):
    #   Draws a number then takes the multiplier to size it.
    #   Height = 50
    #   Width = 30
    origpos = turtle.pos()
    if position:
        turtle.setpos(position)
    turtle.setheading(0)
    turtle.right(90)
    turtle.pd()
    turtle.forward(50*mult)
    turtle.right(180)
    turtle.pu()
    turtle.forward(30*mult)
    turtle.pd()
    turtle.left(90)
    turtle.forward(20*mult)
    turtle.right(90)
    turtle.forward(20*mult)
    turtle.pu()
    return origpos

def draw5(mult=1, position=None):
    #   Draws a number then takes the multiplier to size it.
    #   Height = 50
    #   Width = 60
    origpos = turtle.pos()
    if position:
        turtle.setpos(position)
    turtle.setheading(0)
    turtle.pd()
    turtle.forward(30*mult)
    turtle.forward(-30*mult)
    turtle.right(90)
    turtle.forward(20*mult)
    turtle.left(90)
    turtle.forward(30*mult)
    turtle.right(90)
    turtle.forward(20*mult)
    turtle.right(90)
    turtle.forward(30*mult)
    turtle.pu()
    return origpos

def draw7(mult=1, position=None):
    #   Draws a number then takes the multiplier to size it.
    origpos = turtle.pos()
    if position:
        turtle.setpos(position)
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(50*mult)
    turtle.forward(-50*mult)
    turtle.right(90)
    turtle.forward(30*mult)
    turtle.pu()
    return origpos

def draw9(mult=1, position=None):
    #   Draws a number then takes the multiplier to size it.
    origpos = turtle.pos()
    if position:
        turtle.setpos(position)
    turtle.setheading(0)
    turtle.right(90)
    turtle.pd()
    turtle.forward(50*mult)
    turtle.forward(-50*mult)
    turtle.right(90)
    turtle.forward(30*mult)
    turtle.left(90)
    turtle.forward(20*mult)
    turtle.left(90)
    turtle.forward(30*mult)
    turtle.pu()

