from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Tkinter checkboxes")
root.geometry("400x400")

def show():
	myLabel = Label(root, text=var.get()).pack()





#var = IntVar()
var = StringVar()

c = Checkbutton(root, text="Check this box for a pizza", variable=var, onvalue="Pizza", offvalue="No Pizza")
c.deselect() # due to the bug
c.pack()
#note a funny bug, hence used deselect above
#myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Show selection", command=show).pack()


root.mainloop()