from tkinter import *

myroot = Tk()
myroot.geometry('200x200')
myroot.resizable(0,0)

myroot.bind('<Key-a>', lambda e: myroot.configure(background='LightBlue')) #press a
myroot.bind('<Key-b>', lambda e: myroot.configure(background='Lightpink')) #press b
myroot.bind('<Key-c>', lambda e: myroot.configure(background='Lightgreen'))#press c

mybtn1 = Button(myroot, text='click me !!!')
mybtn1.bind('<Button>', lambda e: myroot.configure(background="blue"))
mybtn1.bind('<ButtonRelease>', lambda e: myroot.configure(background="red"))
mybtn1.pack()

myroot.mainloop()