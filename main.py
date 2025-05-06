import turtle


screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('pink')
t=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t2.penup()
t2.goto(0,200)
t2.pendown()
FORCE_FACTOR = 30
#introsreen
t2.penup()
t2.goto(0, 100)
t2.pendown()
t2.write("all about me", font=('Arial', 30, "normal"), align="center")
t2.penup()
t2.goto(0, -100)
t2.pendown()
t2.write("click enter to go from page to page!", font=('Arial', 30, "normal"), align="center")
t.penup()
t.goto(0, -350)
t.pendown()
t.begin_fill()
t.fillcolor('hot pink')
t.pencolor('hot pink')
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)
t.forward(150)
t.left(90)
t.forward(150)


t.end_fill()




#2nd screen
round = input("Press Enter to Continue: ")
t2.clear()
t.clear()

screen.bgcolor('yellow')

t2.write("hobbies", font=('Arial', 30, "normal"), align="center")


t2.penup()
t2.goto(0, 100)
t2.pendown()

screen.addshape('guine pig.gif')
t2.shape('guine pig.gif')
t2.stamp()
t2.shape('classic')

t2.penup()
t2.goto(0, 50)
t2.pendown()
t2.write("holding my guinea pig", font=('Arial', 10, "normal"), align="center")

t.penup()
t.goto(175, 200)
t.pendown()
screen.addshape('volleyball.gif')
t.shape('volleyball.gif')
t.stamp()
t.shape('classic')

t2.penup()
t2.goto(175, 75)
t2.pendown()
t2.write("practicing volleyball", font=('Arial', 10, "normal"), align="center")

t.penup()
t.goto(175, -200)
t.pendown()
screen.addshape('running.gif')
t.shape('running.gif')
t.stamp()
t.shape('classic')

t2.penup()
t2.goto(175, -100)
t2.pendown()
t2.write("running", font=('Arial', 10, "normal"), align="center")

t.penup()
t.goto(-200, 200)
t.pendown()
screen.addshape('bed.gif')
t.shape('bed.gif')
t.stamp()
t.shape('classic')

t2.penup()
t2.goto(-200, 300)
t2.pendown()
t2.write("sleeping", font=('Arial', 10, "normal"), align="center")


t2.penup()
t2.goto(-100,-200)
t2.pendown()
t2.setheading(100)
t2.fillcolor('white')
t2.pencolor('white')
t2.begin_fill()

t2.forward(100)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(100)

t2.end_fill()


round = input("Press Enter to Continue: ")
t2.clear()
t.clear()

screen.bgcolor('purple')

t2.write("favorite food", font=('Arial', 30, "normal"), align="center")

t.pencolor('white')
t.penup()
t.goto(0, 0)
t.pendown()

screen.addshape('sushi.gif')
t.shape('sushi.gif')
t.stamp()
t.shape('classic')

t2.penup()
t2.goto(0, -100)
t2.pendown()
t2.write("sushi", font=('Arial', 10, "normal"), align="center")

t.penup()
t.goto(100, 200)
t.pendown()
screen.addshape('4.gif')
t.shape('4.gif')
t.stamp()
t.shape('classic')

t2.penup()
t2.goto(175, 75)
t2.pendown()
t2.write("pizza", font=('Arial', 10, "normal"), align="center")

t.penup()
t.goto(-175, 200)
t.pendown()
screen.addshape('macn.gif')
t.shape('macn.gif')
t.stamp()
t.shape('classic')

t2.penup()
t2.goto(-230,150 )
t2.pendown()
t2.write("Mac n cheese", font=('Arial', 10, "normal"), align="center")





t.penup()
t.goto(-200, 0)
t.pendown()
t.fillcolor('yellow')
t.pencolor('yellow')
t.begin_fill()
t.circle(25)
t.setheading(0)
t.circle(25)
t.setheading(90)
t.circle(25)
t.setheading(180)
t.circle(25)
t.setheading(270)


t.end_fill()

round = input("Press Enter to Continue: ")
t2.clear()
t.clear()

screen.bgcolor('light blue')
t2.penup()
t2.goto(0, 0)
t2.pendown()
t2.write("favorite movie", font=('Arial', 30, "normal"), align="center")

t.penup()
t.goto(-175, 200)
t.pendown()
screen.addshape('paranormal.gif')
t.shape('paranormal.gif')
t.stamp()
t.shape('classic')
t2.penup()
t2.goto(175, 200)
t2.pendown()
t2.write("Paranormal Activity", font=('Arial', 15, "normal"), align="center")

t.penup()
t.goto(0, -150)
t.pendown()
t.fillcolor('yellow')
t.pencolor('yellow')
t.begin_fill()
t.fillcolor('dark blue')
t.pencolor('dark blue')
t.begin_fill()
t.circle(100)
t.setheading(90)
t.end_fill()



round = input("Press Enter to Continue: ")
t2.clear()
t.clear()

screen.bgcolor('orange')
t2.penup()
t2.goto(0,0)
t2.pendown()
t.penup()
t.goto(0,0)
t.pendown()
t2.write("favorite sport", font=('Arial', 30, "normal"), align="center")

t.penup()
t.goto(-100, 200)
t.pendown()
screen.addshape('football.gif')
t.shape('football.gif')
t.stamp()
t.shape('classic')




t.penup()
t.goto(0,-100)
t.pendown()
t.write("I like to watch football", font=('Arial', 30, "normal"), align="center")

t.penup()
t.goto(0, -200)
t.pendown()
t.begin_fill()
t.fillcolor('pink')
t.pencolor('pink')
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()





































































turtle.done()