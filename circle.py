import turtle

t=turtle.Turtle()
turtle.title("for me")

screen = turtle.Screen()
screen.bgcolor("black")

#Drawing heart 
t.color("red")
t.fillcolor("black")
t.begin_fill()

t.circle(120)

t.end_fill()

#writing text 
t.up()
t.setpos(-80, 100)
t.down()
t.color('red')
t.write("I LOVE YOU",font=("Algerian",20,"bold"))

t.ht()

turtle.mainloop()