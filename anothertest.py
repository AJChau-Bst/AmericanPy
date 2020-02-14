import tkinter

window = Tk()
window.title("OPR v DPR v CCWM")
window.geometry('800x600'

def hi():
    print(startEntry.get())


window=tkinter.Tk()

startLabel =tkinter.Label(window,text="Enter Star: ")
startEntry=tkinter.Entry(window)


startLabel.pack()
startEntry.pack()

plotButton= tkinter.Button(window,text="plot", command=hi)

plotButton.pack()
        
#Enter in the Year

variable = StringVar(window)
variable.set("2019") # default value
w = OptionMenu(window, variable, "2002", "2003", "2019")
w.pack()


#call a function after okay button
def ok():
    year = variable.get()
    print (year)


#ok button
button = Button(window, text="Year OK", command=ok)
button.pack()

window.mainloop()
