from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)     # use Keyword_argument rather than Positional_argument, for other user to users to understand the values
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-80, -40, -0, 40, 80, 120]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-235, y=y_position[turtle_index])


# leo = Turtle(shape="turtle")
# leo.penup()
# leo.goto(x=-235, y=-60)
#
# rap = Turtle(shape="turtle")
# rap.penup()
# rap.goto(x=-235, y=-90)
#
# don = Turtle(shape="turtle")
# don.penup()
# don.goto(x=-235, y=90)
#
# splint = Turtle(shape="turtle")
# splint.penup()
# splint.goto(x=-235, y=60)
#
# hc = Turtle(shape="turtle")
# hc.penup()
# hc.goto(x=-235, y=30)


screen.exitonclick()


