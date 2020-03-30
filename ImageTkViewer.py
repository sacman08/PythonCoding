import sys
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("TK Fast Image Viewer")

#TODO Make the browse button work and the image list dynamic to pick photos in a directory.
myimg = Image.open("IMG_5556.jpg")
myimg= myimg.resize((250,250), Image.ANTIALIAS)
myimg = ImageTk.PhotoImage(myimg)
imgList=[myimg]


my_label= Label(image = imgList)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_foward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = imglist[image_number-1])
    button_forward = Button(root, text=">>", command=(lambda: forward(image_number+1)))
    button_back = Button(root, text ="<<", command=(lambda: back(image_number-1)))

    if image_number == max(image_number):
        button_forward = Button(root, text=">>", state=DISABLED)
                         
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column= 3)
                         
def back(image_number):
    global my_label
    global button_foward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = imglist[image_number-1])
    button_forward = Button(root, text=">>", command=(lambda: forward(image_number+1)))
    button_back = Button(root, text ="<<", command=(lambda: back(image_number-1)))

    if image_number == max(image_number):
        button_back = Button(root, text="<<", state=DISABLED)
                         
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column= 3)


button_back = Button(root, text="<<", command=back)
button_browse = Button(root, text="...")
button_exit = Button(root, text="Exit", command=root.quit)
button_forward= Button(root, text=">>", command= lambda: forward(2))


button_back.grid(row=1, column=0)
button_browse.grid(row=1, column = 1)
button_exit.grid(row=1, column=2)
button_forward.grid(row=1, column= 3)

root.mainloop()
#TODO if the image is larger than the actual screen size, resize border view to make it fit.
#TODO if image is larger, measure the size and then add sliders to move pic around.
#TODO add zoom in and out function to resize the image temporarily for viewing.
