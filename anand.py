

from easygui import *
import sys


while 1:
    msgbox("Hello, India!")

    msg ="choose shopping site according to you"
    title = "shopping purpose"
    choices = ["amazon","flipcard","mantra"]
    choice = choicebox(msg, title, choices)
    msgbox("You chose: " + str(choice), "Survey Result")
    if choice=="amazon":
       msgbox("hello amazon")
       msg ="choose product"
       title="product detail"
       choices1=["shoes","laptop"]
       choice1=choicebox(msg,title,choices1)
       if choice1=="shoes":
           msgbox("shoes price")
       else:
           msgbox("laptop price")
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)


