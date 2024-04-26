from tkinter import *

myroot = Tk()
myroot.title("Fruit Selection")
myroot.geometry('300x200')

myvar = StringVar()
myvar.set('select')

myselection = OptionMenu(myroot, myvar, "mango", 'apple', 'litchi', 'banana')
myselection.pack()

def mydisplay():
    print("The chosen value:", myvar.get())

mybtn_show = Button(myroot, text="myshow", command=mydisplay)
mybtn_show.pack(pady=30, side=LEFT, anchor=N)

myroot.mainloop()
