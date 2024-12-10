from tkinter import *

def NewFile():
    print("New File!")
def About():
    print("This is a simple example of a menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Ten", menu=filemenu)
filemenu.add_command(label="ho va ten", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="exit", comman=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="mật khẩu", menu=helpmenu)
helpmenu.add_command(label="mât khau:.", command=About)

mainloop()
