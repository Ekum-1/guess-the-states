import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

def coordinates(correct_answer):
    # Retrieve the row corresponding to the correct answer
    row = (data[data.state == correct_answer])
    x = int(row.x)
    y = int(row.y)

    # Create a new turtle to write the state name at the correct coordinates
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle() # Hide the turtle shape
    state_turtle.penup() # Do not draw a line when moving to the coordinates
    state_turtle.goto(x, y) # Move the turtle to the state's coordinates
    state_turtle.write(correct_answer, align="center", font=("Arial", 8, "normal")) # Write the state's name


correct_guesses = 0
guess_list = []

while len(guess_list) < 50:
    answer_state = screen.textinput(title=f"{correct_guesses} States Correct", prompt="What's another State's name?",).title()
    if answer_state == "exit":
        break
    if answer_state in data["state"].values and answer_state not in guess_list:
        coordinates(answer_state)
        guess_list.append(answer_state)
        correct_guesses += 1

screen.exitonclick()