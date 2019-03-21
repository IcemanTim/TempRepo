#!/usr/bin/env python3

from tkinter import *
import string
from random import randint

def change(event, widget):
	global colours
	num = randint(0, len(colours)-1)
	colour = colours[num][3]
	print(colour)
	widget["text"] = "My colour now is \"" + colour + "\""
	widget["bg"] = colour

def show_msg(event):
    print ("Second Button!")

def add_two_buttons(event):
	But = Button(root, text="Press and change the label's colour!")
	But.bind('<Button-1>', lambda event: change(event, Txt))
	But.grid(row=0, column=0, sticky=E+W+S+N)

	Txt = Label(root, text="I'm white now", bg="white")
	Txt.grid(row=0, column=1, sticky=E+W+N+S)

	Exit = Button(root, text="Quit!", command=root.quit)
	Exit.grid(row=0, column=2, sticky=E+W+S+N)

TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.pack(fill=BOTH, expand=True)

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
