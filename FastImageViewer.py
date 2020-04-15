from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

#TODO if the image is larger than the actual screen size, resize border view to make it fit.
#TODO if image is larger, measure the size and then add sliders to move pic around.
#TODO add zoom in and out function to resize the image temporarily for viewing.
#TODO Make the browse button work and the image list dynamic to pick photos in a directory.

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Fast Image Viewer")
        self.minsize(640, 480)
        self.labelFrame = ttk.LabelFrame(self, text = "Open Image File")
        self.labelFrame.grid(column = 3, row = 3, padx=20, pady = 20)
        self.browseButton()



    def browseButton(self):
        self.browseButton = ttk.Button(self.labelFrame, text = "Browse...")
        self.browseButton.grid(column = 3, row = 4, )




if __name__ == '__main__':
    root = Root()
    root.mainloop()