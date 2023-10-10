import turtle

t=turtle.Turtle()
turtle.title("rectangle")

screen = turtle.Screen()
screen.bgcolor("black")

#Drawing rectangle
t.color("red")
t.fillcolor("black")
t.begin_fill()

t.left(180)
t.forward(200)
t.right(90)
t.forward(180)
t.right(90)
t.forward(200)
t.right(90)
t.forward(180)

t.end_fill()

#writing text 
t.up()
t.setpos(-180, 90)
t.down()
t.color('red')
t.write("I LOVE ARTIFICIAL INTELLIGENCE",font=("Verdana",7,"bold"))

t.ht()

turtle.mainloop()