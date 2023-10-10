import turtle

t=turtle.Turtle()
turtle.title("my circles")

screen = turtle.Screen()
screen.bgcolor("black")

#Drawing heart 
t.color("red")
t.fillcolor("black")
t.begin_fill()

t.circle(90)

t.right(90)
t.circle(90)

t.right(90)
t.circle(90)

t.right(90)
t.circle(90)

t.right(135)
t.circle(90)

t.right(180)
t.circle(90)

t.right(90)
t.circle(90)

t.right(180)
t.circle(90)

t.end_fill()

t.ht()

turtle.mainloop()