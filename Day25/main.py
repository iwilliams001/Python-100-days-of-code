import turtle
import pandas
from game_mechanism import StateOnMap

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict('list')

screen = turtle.Screen()
screen.setup(width=725, height=491)
writer = StateOnMap()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while writer.score < 50:
    answer_state = screen.textinput(title=f"{writer.score}/50 States Correct",
                                    prompt="What is another state's name? ").title()
    if answer_state in data_dict["state"]:
        state_index = data_dict["state"].index(answer_state)
        x = data_dict["x"][state_index]
        y = data_dict["y"][state_index]
        writer.write_down(answer_state, x, y)
        writer.update_score()
