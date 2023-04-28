from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

#W-move forward
def move_forward():
    tim.forward(10)
#S-move backward
def move_backward():
    tim.backward(10)
#A-counter-clockwise
def move_counter_clockwise():
    tim.circle(50)

#D-clockwise
def move_clockwise():
    tim.circle(-50)
#C-clear-drawings
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
# screen.onkey(key="space", fun=move_forward)    # high order function

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()


