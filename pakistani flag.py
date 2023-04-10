import turtle

win=turtle.Screen()
win.setup(width=700, height=650)

t=turtle.Turtle()
t.penup()
t.goto(-50,20)
t.pendown()

#green part
t.begin_fill()
t.fillcolor("green")
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()

#white part
t.begin_fill()
t.fillcolor("white")
t.right(180)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.end_fill()

#stick
t.begin_fill()
t.fillcolor("saddlebrown")
t.right(180)
t.forward(120)
t.left(90)
t.forward(500)
t.right(90)
t.forward(40)
t.left(90)
t.forward(15)
t.left(90)
t.forward(100)
t.left(90)
t.forward(15)
t.left(90)
t.forward(40)
t.right(90)
t.forward(500)
t.end_fill()

#circle
t.begin_fill()
t.fillcolor("white")
t.penup()
t.goto(160,115)
t.pendown()
t.circle(70)
t.end_fill()

t.penup()
t.fillcolor('green')
t.goto(185,125)
t.begin_fill()
t.circle(70)
t.end_fill()

# stars
t.penup()
t.fillcolor("white")
t.begin_fill()
t.goto(110,115)
for i in range(0,5):
    t.forward(40)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-30,240)
t.write("Pakistan Zindabad",font="timesnewroman 24 bold")
t.pendown()

t.hideturtle()


turtle.done()