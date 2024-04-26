from tkinter import *
myroot = Tk()
myroot.geometry('300x300')
mypw1 = PanedWindow(myroot)
mypw1.pack(fill=BOTH, expand=1)
mye1 = Entry(mypw1, bd=5, relief=GROOVE,bg="Lightblue")
mypw1.add(mye1)

mypw2 = PanedWindow(mypw1, orient=VERTICAL)
mypw1.add(mypw2)

mye2 = Spinbox(mypw2, from_=10, to=20, font=('calibri',12), bg='Lightpink')

mye3 = Entry(mypw2, bg='Lightgreen', font=('calibri',12))
mye3.insert(0,'12')

mypw1.configure(sashrelief=RAISED)

def subtract():
    mye1.
    num1 = int(mye2.get())
    num2 = int(mye3.get())
    mydata = str(num1-num2)
    mye1.insert(1,mydata)

mypw2.add(mye2)
mypw2.add(mye3)

mybtn = Button(mypw2, text='substract', command=subtract)

mypw2.add(mybtn)

myroot.mainloop()
