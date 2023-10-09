import turtle

# setup turtle window
turtle.setup(800, 400)

def draw_B():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)

def draw_A():
    turtle.left(60)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(60)

def draw_D():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(20)
    turtle.forward(20)
    turtle.right(20)
    turtle.forward(20)
    turtle.right(20)
    turtle.forward(20)
    turtle.right(20)
    turtle.forward(20)
    turtle.right(20)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(100)

def draw_R():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(70)

def draw_I():
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)

# Draw B
draw_B()
turtle.penup()
turtle.right(90)
turtle.forward(120)
turtle.left(90)
turtle.pendown()

# Draw A
draw_A()
turtle.penup()
turtle.right(60)
turtle.forward(10)
turtle.pendown()

# Draw D
draw_D()
turtle.penup()
turtle.right(180)
turtle.forward(120)
turtle.pendown()

# Draw R
draw_R()
turtle.penup()
turtle.left(45)
turtle.forward(120)
turtle.right(90)
turtle.pendown()

# Draw I
draw_I()

# Hide the turtle cursor
turtle.hideturtle()

# keep the turtle graphics window open
turtle.done()