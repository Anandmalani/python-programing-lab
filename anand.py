#ANAND MALANI
#ROLL NO. 37
#GR NO.  11810791


from easygui import *
import sys
list1=[]
sum =0
while 1:
    msgbox("Hello, India!")

    msg ="choose shopping site according to you"
    title = "shopping purpose"
    choices = ["amazon","flipcard"]
    choice = choicebox(msg, title, choices)
    msgbox("You chose: " + str(choice), "Survey Result")
    if choice=="amazon":
       msgbox("hello amazon")
       msg ="choose product"
       title="product detail"
       choices1=["shoes","laptop"]
       choice1=choicebox(msg,title,choices1)
       if choice1=="shoes":
           m ="shoes price = 2000\n"
           msgbox(m)
	   list1.append(m)
	   sum += 2000
           #msgbox("total price= 2000")
           
       elif choice1=="laptop":
            n="laptop price=35000\n"
            msgbox(n)
            list1.append(n)
            sum += 35000 
           #sgbox("laptop price=35000") 
           
    else:
       msgbox("hello flipcard")
       msg ="choose product"
       title="product detail"
       choices2=["laptop","mobile"]
       choice2=choicebox(msg,title,choices2)
       if choice2=='mobile':
           p="mobile price = 3000\n"
           msgbox(p)
           list1.append(p)
           sum += 3000
           #msgbox("total price= 3000")

       elif choice2=="laptop":
            u="laptop price=35000\n"
            msgbox(u)
            list1.append(u)
            sum += 35000 
           #sgbox("laptop price=35000")
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
	textbox('Purchase memo', 'Bill Desk',list1)
        sys.exit(0)


