from tkinter import *


class Mydeletetest(Tk):
    def __init__(self):
        super().__init__()
        self.title('Delete Example')
        self.mye1= Entry(self, font=('Helvetica',12), width=30, bd=5)
        self.mye1.focus()
        self.mye1.pack(side=LEFT, padx=10)

        self.btn1 = Button(self, text='Delete the text', command=lambda: mydelete(self, self.mye1))
        #self.btn1.focus()
        self.btn1.pack(pady=40)

        def mydelete(self, myentry):
            myentry.delete(first=0,last=15)


if __name__ == "__main__":
    myroot = Mydeletetest()
    myroot.geometry('400x100')
    myroot.mainloop()


