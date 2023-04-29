import turtle
from turtle import Turtle, Screen
import random



is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)     # use Keyword_argument rather than Positional_argument, for other user to users to understand the values
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-80, -40, -0, 40, 80, 120]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    if turtle.xcor() > 230:
        is_race_on = False
        winning_color = turtle.pencolor()
        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
        else:
            print(f"You've lose! The {winning_color} turtle is the winner!")


    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()


