import turtle
import pandas
sc=turtle.Screen()
sc.title("US States Games")
sc.setup(750,500)
sc.bgpic("blank_states_img.gif")
data=pandas.read_csv("50_states.csv")
tim=turtle.Turtle()
tim.penup()
tim.shape("triangle")
tim.speed("slow")
allstate=data.state.tolist()
print(allstate)
Game_is_on=True
State_done=[]
while Game_is_on:
    guess = sc.textinput(title=f"Guess the state {len(State_done)}/50",prompt="enter the state")
    guess=guess.title()
    if guess=="Exit":
        break
    if guess in allstate and guess not in State_done:
       State_done.append(guess)

       tim.goto(int(data.x[data.state== guess]),int(data.y[data.state== guess]))
       tim.write(guess,font=('Arial', 10, 'normal'))
       print(State_done)
    if len(State_done)==50:
        Game_is_on=False

# sc.addshape("blank_states_img.gif")
# turtle.shape("blank_states_img.gif")
# turtle.color("red")
# turtle.forward(500)



#sc.exitonclick()