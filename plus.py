import turtle

t=turtle.Turtle()
turtle.title("plus")

screen = turtle.Screen()
screen.bgcolor("black")

#Drawing rectangle
t.color("red")
t.fillcolor("black")
t.begin_fill()

t.left(180)
t.forward(100)
t.left(90)
t.forward(180)
t.right(90)
t.forward(100)
t.right(90)
t.forward(180)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)

t.end_fill()

#writing text 
t.up()
t.setpos(-60,-80)
t.down()
t.color('red')
t.write("I LOVE THE LORD OUR GOD OF ALL CREATION,",font=("Verdana",7,"bold"))
t.setpos(-60,-90)
t.write("JESUS CHRIST OUR SAVIUOR WHO DIED FOR OUR SINS",font=("Verdana",7,"bold")) 
t.setpos(-60,-100)
t.write("AND THE HOLY SPIRIT WHO CONTROL AND GUIDE US IN OUR DAILY BASIS.",font=("Verdana",7,"bold"))

t.ht()

turtle.mainloop()