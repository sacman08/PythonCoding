import sys
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import filedialog

#TODO if the image is larger than the actual screen size, resize border view to make it fit.
#TODO add zoom in and out function to resize the image temporarily for viewing.
#TODO After browse selection, KeyError: 'File name' Unable to getmodebase or getmode on image file
#TODO May need to use Image.open or a parser to just display file.

#Build the root image viewing window
root = Tk()

#Build the content on the frame for navigation
content = ttk.Frame(root)
content.grid(column=0, row=0)
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=0)


#Create the zoom variables for the menu
sizecodes = ('Zoom','200%','175%','150%','125%','100%','75%','50%','25%')
sizevar = StringVar()
#osp = os.path.expanduser(r'~'+os.getlogin())
# After browsing set the directory and find all image files (Do I even need this loop now?)
#for file in os.listdir(osp):
#    if file.endswith(".jpg"):
#        myimg=(os.path.join(osp, file))
#        myimg.show()
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

    #if image_number == max(image_number):
    #    button_forward = Button(root, text=">>", state=DISABLED)
                         
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

    #if image_number == max(image_number):
    #    button_back = Button(root, text="<<", state=DISABLED)
                         
    my_label.grid(row=0, column=0, columnspan=5)
    button_back.grid(row=4, column=0)
    button_forward.grid(row=4, column= 1)

def browse():
    filename = filedialog.askopenfilename(initialdir = r"/", title="Select A File", filetype = (("jpeg", "*.jpg"), ("All Files", "*.*"))) 
    #imgList = ImageTk.PhotoImage(image=filename)
    #imgList.show()
    #imgList = Image.open(filename)  #Image.open uses the OS default image viewer program (i.e. Windows Preview)
    #imgList.show()
    #imgList = ImageTk.PhotoImage(myimg)
    #show first image selected
    
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
