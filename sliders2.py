from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Tkinter sliders")
root.geometry("400x800") #initial window size

# the scale widget
vertical = Scale(root, from_=0, to=200)
vertical.pack() 


# get the numbers horizontal

def slide(var):
	my_label = Label(root, text=horizontal.get()).pack()
	

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=slide) #passing output to the slide function
horizontal.pack()





root.mainloop()
