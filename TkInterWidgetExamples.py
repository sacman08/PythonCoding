from tkinter import *

root = Tk()
root.option_add('*tearOff', FALSE)

win = Toplevel(root)
menubar = Menu(win)
win['menu'] = menubar

menubar = Menu(win)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')

menu_file.add_command(label='New', command=newFile)
menu_file.add_command(label='Open...', command=openFile)
menu_file.add_command(label='Close', command=closeFile)

root.mainloop()
