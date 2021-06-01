from tkinter import *

root = Tk()
root.title("Calculator")


e = Entry(root, width=35, borderwidth=10) # entry field for numbers
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #since the grid has three buttons under



def button_clear():
    e.delete(0, END)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    
    e.insert(0, str(current) + str(number)) #convert to a string so they don't get added together

def button_add():
    global f_num
    global math #what math are we doing?
    math = "addition" #we are doing addition here
    first_number = e.get() #get the first number
    f_num = int(first_number) #store the first number
    e.delete(0, END) #clear the screen

def button_equal(): #here's where we do the maths!
    second_number = e.get() #get the second number
    e.delete(0, END) #clear the screen

    if math == "addition":
        e.insert(0, f_num + int(second_number)) #add them

    if math == "subtraction":
        e.insert(0, f_num - int(second_number)) #subtract

    if math == "multiplication":
        e.insert(0, f_num * int(second_number)) #multiply

    if math == "division":
        e.insert(0, f_num / int(second_number)) #divid

def button_subtract():
    global f_num
    global math #what math are we doing?
    math = "subtraction" #we are doing subtraction here
    first_number = e.get() #get the first number
    f_num = int(first_number) #store the first number
    e.delete(0, END) #clear the screen
    

def button_multiply():
    global f_num
    global math #what math are we doing?
    math = "multiplication" #we are doing multiplication here
    first_number = e.get() #get the first number
    f_num = int(first_number) #store the first number
    e.delete(0, END) #clear the screen

def button_divide():
    global f_num
    global math #what math are we doing?
    math = "division" #we are doing division here
    first_number = e.get() #get the first number
    f_num = int(first_number) #store the first number
    e.delete(0, END) #clear the screen
    

    
    


# define the buttons buttons
button_1 = Button(root, text="1", padx=50, pady=25, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=50, pady=25, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=50, pady=25, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=50, pady=25, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=50, pady=25, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=50, pady=25, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=50, pady=25, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=50, pady=25, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=50, pady=25, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=50, pady=25, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=50, pady=25, bg="lightgray", command=button_add)
button_equals = Button(root, text="=", padx=109, pady=25, bg="lightgray", command=button_equal)
button_clear = Button(root, text="Clear", padx=100, pady=25, bg="lightgray", command=button_clear)

button_subtract = Button(root, text="-", padx=51, pady=25, bg="lightgray", command=button_subtract)
button_multiply = Button(root, text="*", padx=51, pady=25, bg="lightgray", command=button_multiply)
button_divide = Button(root, text="/", padx=51, pady=25, bg="lightgray", command=button_divide)

#buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equals.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)



