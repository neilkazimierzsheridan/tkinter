from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Tkinter sliders")
root.geometry("400x400") #initial window size

# the scale widget
vertical = Scale(root, from_=0, to=200)
vertical.pack() 

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

# get the numbers from them!

#my_label = Label(root, text=horizontal.get()).pack()

def slide():
	my_label = Label(root, text=horizontal.get()).pack()
	#use to change the window size
	root.geometry(str(horizontal.get()) + "x400")





my_btn = Button(root, text="Click Here!", command=slide).pack()

root.mainloop()
