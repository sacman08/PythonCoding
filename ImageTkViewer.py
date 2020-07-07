#! /usr/bin/python
import sys
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import filedialog

#TODO Give it a default image to display on opening with app info and contacts
#TODO if the image is larger than the actual screen size, resize view to make it fit.
#TODO Image.resize generates error about no attribute available to resize
#TODO Remove Previous image so that it is not "underneath" current image.
#TODO add zoom in and out function to resize the image temporarily for viewing.
#TODO convert sizevar selection to proper scale (i.e. 200% = 2, 175% = 1.75)
#(Paused) TODO Compile images into a way to select next and previous OR remember last images selected to allow for back to and forward to movement.


#Build the root image viewing window
root = Tk()
root.wm_title("Fast Image Viewer")
root.geometry("640x480")
#Build the content on the frame for navigation
content = ttk.Frame(root)
content.grid(column=0, row=0)
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=0)


#Create the zoom variables for the menu
sizecodes = ('Zoom','200%','175%','150%','125%','100%','75%','50%','25%')
sizevar = StringVar()
#Create Image variables for opening images
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
    global my_label
    global imgList
    global browse
    global root
    imgList.image = None  #Reset image
    filename = filedialog.askopenfilename(initialdir = r"/", title="Select A File", filetype = (("jpeg", "*.jpg"), ("All Files", "*.*"))) 
    imgList = ImageTk.PhotoImage(Image.open(filename))
    my_label= Label(image = imgList, text=filename)
    my_label.image = imgList
    my_label.grid(row=1, column=0, columnspan=5)
    zoom(imgList) # call Zoom funciton to check image size
    imgList.resize(newsize)
    root.geometry(str(imgList.width())+"x"+str(imgList.height()+30))    # Set the root window size to the image size plus 30 for buttons at bottom.
    #if imgList.width() > 800 : #If my image is too big, attempt to scale or fit inside display window (1366x756)
    #   my_label= Label(image = imgList, text=filename)
    #   my_label.image = imgList
    #   my_label.grid(row=1, column=0, columnspan=5)
    #   root.geometry(imgList.width+"x"+imgList.height+10)
        #root.geometry("800x600")  resizes main window but crops off buttons and most of image outside width,height
        
        
    #else:  #Show my image in original size (can be larger than display screen of computer and overlaps (?) browse and exit buttons.
    #   my_label= Label(image = imgList, text=filename)
    #   my_label.image = imgList
    #   my_label.grid(row=1, column=0, columnspan=5)           

    
    
def zoom(newsize):
    global zoom
    global sizevar
    global my_label
    global root
    sizevar_dict = {'200%' : 2, '175%': 1.75,'150%': 1.5, '125%':1.25,'100%': 1,'75%': .75,'50%': .5,'25%': .25}
    if imgList.width() > 1024:   # Is image wider that most visible monitor displays?
        imgWidth = imgList.width() / 1024  # Get the factor it is larger
        imgWidfactor = (float(imgWidth - int(imgWidth)))  # get the float values greater than 1
        newsize = (imgList.width() * (imgWidfactor), imgList.height() * (imgWidfactor)) # create new image size reducing by factor
        print(imgWidfactor, newsize)
        #imgList = Image.resize(newsize)  # reduce image size
        return newsize # Return to browse function with new image size  
    #if imgList.height() > 640:
    #    imgHeight = imgList() / 640
    #    imgHthFactor = float(imgHeight - int(imgHeight))  
    
    
    


#Style the grid
my_label.grid(row=0, column=0, columnspan=5)
#button_back = Button(root, text="<<", command=back)
#button_forward= Button(root, text=">>", command= lambda: forward(2))
#button_zoom= ttk.Combobox(root, textvariable=sizevar)
#button_zoom['values']=(sizecodes)
#button_zoom.current(0)
button_browse = Button(root, text="Browse...", command=browse)
button_exit = Button(root, text="Exit", command=root.quit)
imgList = ImageTk.PhotoImage(Image.open("FastImageViewer_Default.jpg"))
#TODO Current working directory for default image open?

#Place the buttons
#button_back.grid(row=4, column=0)
#button_forward.grid(row=4, column=1)
#button_zoom.grid(row=4, column=2)
button_browse.grid(row=4, column=3)
button_exit.grid(row=4, column=4)
my_label.image = imgList
my_label.grid(row=1, column=0, columnspan=5)

root.mainloop()
