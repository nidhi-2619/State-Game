import turtle
import pandas as pd
import csv

screen = turtle.Screen()
screen.title('US State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# we need to get the coordinates on the map so we use
player_Score = []
us_data = pd.read_csv('50_states.csv')
states = us_data.state.to_list()
while len(player_Score) < 50:
    answer = screen.textinput(title=f'{len(player_Score)}/50 Your Score',prompt='What is the name of another state').title()
    if answer == 'Exit':
        unscored_states = []
        for state in states:
            if state not in player_Score:
                unscored_states.append(state)
        missed_states = pd.DataFrame(unscored_states)
        missed_states.to_csv('missed_states.csv')
        break

    if answer in states:
        player_Score.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        valid = us_data[us_data.state == answer]
        t.goto(float(valid.x), float(valid.y))
        t.write(valid.state.item())


screen.exitonclick()