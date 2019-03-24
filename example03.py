#!/usr/bin/env python3

from tkinter import *
import string
from random import randint

def change(event, widget):
	global colours
	num1 = randint(0, len(colours)-1)
	num2 = randint(0, len(colours)-1)
	colour_bg = colours[num1][3]
	colour_fg = colours[num2][3]
	print(colour_bg," ", colour_fg)
	widget["text"] = "My colour now is "
	widget["bg"] = colour_bg
	widget["fg"] = colour_fg

def show_msg(event):
    print ("Second Button!")

def add_two_buttons(event):
	But = Button(root, text="Press and change the label's colour!")
	But.bind('<Button-1>', lambda event: change(event, BG_Txt))

	BG_Txt = Label(root, text="My colour now is", bg="white")

	Delimeter.grid(row=1, column=0, columnspan=3, sticky=N+S+E+W)
	Txt.grid(row=2, column=0, columnspan=3, sticky=N+S+E+W)

	BG_Txt.grid(row=0, column=1, sticky=E+W+N+S)
	Exit.grid(row=0, column=2, sticky=E+W+S+N)
	But.grid(row=0, column=0, sticky=E+W+S+N)

	root.columnconfigure(2, weight=1)


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
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2,weight=1)

But_Add = Button(root, text="Add")
But_Add.bind('<Button-1>', add_two_buttons)
But_Add.grid(row=0, column=0, sticky=E+W)

Exit = Button(root, text="Quit!", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W)

Delimeter = Label(root, bg="black")
Delimeter.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)

Txt = Label(root, text="This is a label", bg="PeachPuff")
Txt.grid(row=2, column=0, columnspan=2, sticky=E+W+N+S)

#----------------------------------------------------

f = open('colours.txt', 'r')

global colours
colours = []

for line in f:
	l = len(line)
	arr = []
	i = 0
	while i < l:
		mass = ""
		a = line[i]
		while (a != ' ' or a != '\t') and '0' <= a <= '9':
			mass += a
			i += 1
			if i < l:
				a = line[i]
			else:
				break
		if a in string.ascii_letters:
			while a != '\n' and i < l:
				mass += a
				i += 1
				if i < l:
					a = line[i]
		i += 1
		if mass != '':
			if mass.isdigit() :
				arr.append(int(mass))
			else :
				arr.append(mass)
	colours.append(arr)

TKroot.mainloop()
print("Done")
#root.destroy()
