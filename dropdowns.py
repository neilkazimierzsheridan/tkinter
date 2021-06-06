from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Tkinter drop downs")
root.geometry("400x400")

def show():
	myLabel = Label(root, text=clicked.get()).pack()

options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]


clicked = StringVar()
clicked.set(options[0]) #set to begin

drop = OptionMenu(root, clicked, *options)

drop.pack()

myButton = Button(root, text="show selection", command=show).pack()

root.mainloop()