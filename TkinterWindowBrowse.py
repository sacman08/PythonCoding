from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Image Viewer Window")
        self.minsize(640,480)
        self.wm_iconbitmap('icon.ico')













if __name__ == '__main__':
    root = Root()
    root.mainloop()
    
