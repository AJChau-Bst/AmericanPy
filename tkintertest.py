from tkinter import *
import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv


#get some basic windows stuff in first
window = Tk()
window.title("OPR v DPR v CCWM")
window.geometry('800x600')

#Team Number Enter
variable2 = StringVar(window)
L1 = Label(window, text="Team")
L1.pack( side = LEFT)
E1 = Entry(window, bd =5)
E1.pack(side = RIGHT)

#Enter in the Year

variable = StringVar(window)
variable.set("2019") # default value
w = OptionMenu(window, variable, "2002", "2003", "2019")
w.pack()


#call a function after okay button
def ok():
    year = variable.get()
    print (year)
    team = variable2.get()
    print(team)


#ok button
button = Button(window, text="OK", command=ok)
button.pack()

window.mainloop()