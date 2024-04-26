from tkinter import *
from tkinter import Entry


class MouseBtnClick(Tk):
    def __init__(self):
        super().__init__()
        self.title('Button "Left or Right" Click Action')
        myint2 = StringVar()

        def mycall(event):
            print("left clicked")
            myint = "Leftclick"
            myint2.set(myint)
            myshow1()

        def myshow1():
            myroot.configure(background='LightBlue')



        def myshow2():
            myroot.configure(background='pink')

        def mycallme(event):
            print("right clicked")
            myint = "Rightclick"
            myint2.set(myint)
            myshow2()

        self.myb1 = Button(self, text='Leftclick', font=("Helvetica", 15))
        self.myb1.bind('<Enter>', mycall)
        self.myb1.pack(pady=10)

        self.myb2 = Button(self, text='Rightclick', font=("Roman", 15))
        self.myb2.bind('<Leave>', mycallme)
        self.myb2.pack(pady=10)

        self.myb3 = Button(self, text='clickme', font=("Calibri", 15))
        self.myb3.bind('<Button-1>', mycall)
        self.myb3.pack(pady=10)
        self.myb3.bind('<Button-3>', mycallme)
        self.myb3.pack(pady=10)

        self.MyEntry2 = Entry(self, font=('Calibri', 12), textvariable=myint2)
        self.MyEntry2.pack()
        # MyEntry2.configure(state='readonly')

        """self.MyEntry2 = Entry(self, font = ('Calibri', 12), textvariable = myint2)
        self.MyEntry2.pack()
        self.MyEntry2.configure(state = 'readonly')
        """
if __name__ == "__main__":
    myroot = MouseBtnClick()
    myroot.geometry('300x300')
    myroot.configure(background="blue")
    myroot.mainloop()
