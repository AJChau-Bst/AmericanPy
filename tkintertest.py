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


#Enter in the Year

variable = StringVar(window)
variable.set("2019") # default value
w = OptionMenu(window, variable, "2002", "2003", "2019")
w.pack()

#Lists!
Team = []
OPR = []
DPR = []
CCWM = []

#call a function after okay button
def ok():
    year = variable.get()
    print(year)

    yearrequest = str(year)




#ok button
button = Button(window, text="Year OK", command=ok)
button.pack()

with open(year + '.csv') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        Team.append(row[0])
        OPR.append(row[1])
        DPR.append(row[2])
        CCWM.append(row[3])
    #remove the header
    Team.remove(Team[0])
    OPR.remove(OPR[0])
    DPR.remove(DPR[0])
    CCWM.remove(CCWM[0])

window.mainloop()
