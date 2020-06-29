import sys
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image,ImageOps
from tkinter import filedialog

#TODO if the image is larger than the actual screen size, resize border view to make it fit.
#TODO add zoom in and out function to resize the image temporarily for viewing.
#TODO convert sizevar selection to proper scale (i.e. 200% = 2, 175% = 1.75)
#TODO After browse selection, Image is showing in window but blank
#TODO Compile images into a way to select next and previous 

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
    #TODO Compile images into a way to select next and previous                    
    my_label.grid(row=0, column=0, columnspan=5)
    button_back.grid(row=4, column=0)
    button_forward.grid(row=4, column= 1)

def browse():
    filename = filedialog.askopenfilename(initialdir = r"/", title="Select A File", filetype = (("jpeg", "*.jpg"), ("All Files", "*.*"))) 
    imgList = ImageTk.PhotoImage(Image.open(filename))
    #TODO If check to reduce size to fit inside monitor size
    #if imgList.width() > 800 :
    #    ImageOps.scale(imgList, .5)
    #    my_label= Label(image = imgList)
    #    my_label.grid(row=1, column=0)
    #else:
    #    my_label= Label(image = imgList)
    #    my_label.grid(row=1, column=0)       
    my_label= Label(image = imgList, text=filename)
    my_label.grid(row=1, column=0, columnspan=5)     
    #TODO Fix blank image in grid window after "opening" 
    #TODO Display images to fit in display window (i.e. ImageOps.scale down as needed)
    
def zoom():
    pass
    #ImageOps.scale for zooming by size
    #global sizevar
    #TODO convert sizevar tuple to dictionary so I can pull resize by selection (i.e sizevar = sizevar_dict.keys) 
    #sizevar_dict = {'200%' : 2, '175%': 1.75,'150%': 1.5, '125%':1.25,'100%': 1,'75%': .75,'50%': .5,'25%': .25}


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
