# Tkinter widget build test.
# Create frame, add some selection boxes, text box for name, buttons for clicking.
# No other current usage than to show display functions available.

#pull in modules for Tkinter
from tkinter import *
from tkinter import ttk

#Create the root window
root = Tk()

#Build a frame on the root window.
content = ttk.Frame(root)
#Style the frame 
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
#drop the label on the frame.
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

#set the values for variables (to display)
onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

#Build the content to display
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

#grid out the display
content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.mainloop()
