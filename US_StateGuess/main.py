import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)





data_file = pandas.read_csv("50_states.csv")
states = data_file["state"].to_list()

score = 0
correct_states = []


while score != 50:
    answer_state = screen.textinput(title=f"{score}/50 states", prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data_file[data_file.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
        correct_states.append(answer_state)
        score += 1







screen.exitonclick()