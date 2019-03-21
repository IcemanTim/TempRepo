#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''

from tkinter import *

def show_msg(event):
    print ("Second Button!")

def add_two_buttons(event):
	But = Button(root, text="Press and change my colour!")
	But.bind('<Button-1>', show_msg)
	But.grid(row=0, column=0, sticky=E+W+S+N)

	Txt = Label(root, text="My colour now is", bg="PeachPuff")
	Txt.grid(row=0, column=1, sticky=E+W+N+S)

	Exit = Button(root, text="Quit!", command=root.quit)
	Exit.grid(row=0, column=2, sticky=E+W+S+N)

TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.place(relx=0, rely=0, relheight=1, relwidth=1)

width = 780
height = 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
osx = (screen_w - width)/2
osy = (screen_h - height)/2
TKroot.geometry('%dx%d+%d+%d' % (width, height, osx, osy))

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=1)

But_Add = Button(root, text="Add")
But_Add.bind('<Button-1>', add_two_buttons)
But_Add.grid(row=0, column=0, sticky=E+W+S+N)

Exit = Button(root, text="Quit!", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)

BG_label = Label(root, bg="black")
BG_label.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)

Txt = Label(root, text="This is a label", bg="PeachPuff")
Txt.grid(row=2, column=0, columnspan=3, sticky=E+W+N+S)

TKroot.mainloop()
print("Done")
#root.destroy()
