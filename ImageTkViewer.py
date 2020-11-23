#! /usr/bin/python
import sys
#import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import filedialog

#TODO Give it a default image to display on opening with app info and contacts
#TODO Remove Previous image so that it is not "underneath" current image.
#TODO add zoom in and out function to resize the image temporarily for viewing.



#Build the root image viewing window
root = Tk()
root.wm_title("Fast Image Viewer")
root.geometry("640x480")
content = ttk.Frame(root)
content.grid(column=0, row=0)
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=0)


#Create Image variables for opening images
imgList = []
my_label= Label(image = imgList)


#Functions for button controls


def browse():
    global my_label
    global imgList
    global browse
    global root
    global content
    #imgList.image = None  #Reset image
    #my_label.delete()
    filename = filedialog.askopenfilename(initialdir = r"/", title="Select A File", filetype = (("jpeg", "*.jpg"), ("All Files", "*.*"))) 
    my_image = Image.open(filename)
    #Most monitors are wider than 1024 bits so reduce factor to fit
    
    my_image_reduced = my_image.resize((640,355))
        
    imgList = ImageTk.PhotoImage(my_image_reduced)
    my_label= Label(image = imgList, text=filename)
    my_label.image = imgList
    my_label.grid(row=1, column=0, columnspan=5)
   
    image_width = my_image_reduced.size[0]
    image_height = my_image_reduced.size[1]
    root.geometry("{}x{}".format(image_width,image_height+30)) # Set the root window size to the image size plus 30 for buttons at bottom     
    


#Style the grid
my_label.grid(row=0, column=0, columnspan=5)
button_browse = Button(root, text="Browse...", command=browse)
button_exit = Button(root, text="Exit", command=root.quit)
imgList = ImageTk.PhotoImage(Image.open("FastImageViewer_Default.jpg"))
#TODO Current working directory for default image open?

#Place the buttons
button_browse.grid(row=4, column=3)
button_exit.grid(row=4, column=4)
my_label.image = imgList
my_label.grid(row=1, column=0, columnspan=5)

root.mainloop()
