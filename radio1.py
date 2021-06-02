from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio buttons tkinter")


#r = IntVar()
#r.set("2")

#easier way to set the radio buttons

MODES = [
	("Pepperoni","Pepperoni"),
	("Pineapple","Pineapple"),   
	("Cheese","Cheese"),
	("Mushroom","Mushroom"),
]

pizza = StringVar()
pizza.set("Mushroom")

for text, mode in MODES:
	Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)



def clicked(value):
	MyLabel = Label(root, text=value)
	MyLabel.pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack() #these command when click radio
#Radiobutton(root, text="Option 1", variable=r, value=2, command=lambda: clicked(r.get())).pack() #button


#MyLabel = Label(root, text=pizza.get())
#MyLabel.pack()

MyButton = Button(root, text="Click when you have chosen your pizza", command=lambda: clicked(pizza.get()))
MyButton.pack()

root.mainloop()