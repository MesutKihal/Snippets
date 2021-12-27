

from turtle import *

penup()
goto((-200, 200))
# Draw a square
pendown()
for _ in range(4):
    forward(300)
    right(90)
penup()
# Split the square with a line
forward(150)
right(90)
# Fill the rectangle with green
fillcolor("green")
begin_fill()
for i in range(4):
    if i % 2 == 0:
        forward(300)
        right(90)
    else:
        forward(150)
        right(90)

end_fill()
# Draw a red circle
fillcolor("black")
fillcolor("red")
forward(90)
right(90)
begin_fill()
circle(65)
end_fill()
# Draw a white circle
fillcolor("white")
left(90)
forward(120)
left(90)
forward(30)
begin_fill()
circle(55)
end_fill()
# Draw a red star
left(90)
forward(60)
left(90)
forward(20)
right(180)
fillcolor("red")
begin_fill()
for _ in range(5):
    forward(55)
    right(144)
end_fill()
