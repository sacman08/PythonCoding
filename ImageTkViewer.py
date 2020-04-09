import sys
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import filedialog

#TODO if the image is larger than the actual screen size, resize border view to make it fit.
#TODO if image is larger, measure the size and then add sliders to move pic around.
#TODO add zoom in and out function to resize the image temporarily for viewing.
#TODO Make the browse button work and the image list dynamic to pick photos in a directory.


#Build the root window
root = Tk()

#Build the content on the frame
content = ttk.Frame(root)
content.grid(column=0, row=0)
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=0)

#myimg = Image.open("IMG_5556.jpg")
#myimg= myimg.resize((560,480), Image.ANTIALIAS)


#Create the variables for the menu
sizecodes = ('Zoom','200%','175%','150%','125%','100%','75%','50%','25%')
sizevar = StringVar()
osp = os.path.expanduser('~'+os.getlogin())
#find all image files
for file in os.listdir(osp):
    if file.endswith(".jpg"):
        myimg=(os.path.join(osp, file))
        print(myimg)
imgList = []
my_label= Label(image = imgList)

#Functions for menu and picture controls
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
                         
    my_label.grid(row=0, column=0, columnspan=5, rowspan=5)
    button_back.grid(row=4, column=0)
    button_forward.grid(row=4, column= 1)
                         
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
                         
    my_label.grid(row=0, column=0, columnspan=5)
    button_back.grid(row=4, column=0)
    button_forward.grid(row=4, column= 1)

def browse():
    #find login
    #get current path
    #global myimg
    #global imgList
    #find all image files
    self.filename = filedialog.askopenfilename(initialdir = "/", title="Select A File", filetype = (("jpeg", "*.jpg"), ("All Files", "*.*"))) 
    imgList = ImageTk.PhotoImage(myimg)
    #imgList=[myimg]
    
    #show first image
    #pass

def zoom():
    pass

#Style the grid
my_label.grid(row=0, column=0, columnspan=5)
button_back = Button(root, text="<<", command=back)
button_forward= Button(root, text=">>", command= lambda: forward(2))
button_zoom= ttk.Combobox(root, textvariable=sizevar)
button_zoom['values']=(sizecodes)
button_zoom.current(0)
button_browse = Button(root, text="Browse...", command=browse)
button_exit = Button(root, text="Exit", command=root.quit)

#Place the buttons
button_back.grid(row=4, column=0)
button_forward.grid(row=4, column=1)
button_zoom.grid(row=4, column=2)
button_browse.grid(row=4, column=3)
button_exit.grid(row=4, column=4)


root.mainloop()
