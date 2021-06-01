from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("viewing images")
#root.iconbitmap('C:\Users\nksheridan\Downloads\oicon.ico')



#open the images and assign to myimgx
myimg1 = ImageTk.PhotoImage(Image.open("plant.jpg"))
myimg2 = ImageTk.PhotoImage(Image.open("plant2.jpg")) 
myimg3 = ImageTk.PhotoImage(Image.open("plant3.jpg"))
myimg4 = ImageTk.PhotoImage(Image.open("plant5.jpg"))
myimg5 = ImageTk.PhotoImage(Image.open("plant6.jpg"))
myimg6 = ImageTk.PhotoImage(Image.open("plant7.jpg"))
image_list = [myimg1, myimg2, myimg3, myimg4, myimg5, myimg6]
#list of images

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) # E is east

my_label = Label(image=image_list[0])
#my_label = Label(image=myimg1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
   
    my_label.grid_forget() #clear the image
    my_label = Label(image = image_list[image_number-1])
    
    button_forward = Button(root, text=">>forward", command=lambda: forward(image_number+1)) #set the buttons again
    button_back = Button(root, text="<<back", command=lambda: back(image_number-1))
    
    if image_number == 6:
        button_forward = Button(root, text=">>forward", state=DISABLED) #disable if image number is 6

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0) #write the buttons again
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) # E is eaststatus
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)  # display status giving number of image in the image_list

def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])

    button_forward = Button(root, text=">>forward", command=lambda: forward(image_number+1)) #set the buttons again
    button_back = Button(root, text="<<back", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<back", state =DISABLED)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) # E is eaststatus
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)  # display status giving number of image in the image_list



#my_label = Label(image=myimg1)
#my_label = Label(image=image_list[0])
#my_label.grid(row=0, column=0, columnspan=3)



#buttons to move between images

button_back = Button(root, text="<< back", border=5, command=back)
button_quit = Button(root, text="Exit Program", border=5, command=root.destroy)
button_forward = Button(root, text=">> forward", border=5, command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E) #display image number, sticky uses compass west to east



root.mainloop()
