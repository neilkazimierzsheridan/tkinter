from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Tkinter Files")


#root.filename = filedialog.askopenfilename(initialdir="/", title="Select the file", filetypes=(("jpg files","*.jpg"),("png files", "*.png")))
# all files just gonna be "*.*"



def open():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir="/", title="Select the file", filetypes=(("jpg files","*.jpg"),("png files", "*.png")))
	my_label = Label(root, text=root.filename).pack() # display name of chosen file
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = Label(image=my_image).pack() ## display the chosen image file


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()