from tkinter import *


class MyValidate(Tk):
    def __init__(self):
        super().__init__()
        self.myl0 = Label(self, text="enter a number", fg='magenta', font=("Arial",12))
        self.myl0.place(x=10,y=30)

        self.mye1 = Entry(self, font=("helvetica",10))
        self.mye1.place(x=150, y=30)

        self.myl1 = Label(self, text='', fg='red')
        self.myl1.place(x=70,y=50)

        self.myreg = self.register(self.mycallback)
        self.invalidcmd = self.register(self.myinvalid_name)
        self.mye1.config(validate='key', validatecommand=(self.myreg, '%P'), invalidcommand=(self.invalidcmd, '%S'))

    def mycallback(self, myinp):
        if myinp.isdigit():
            print(myinp)
            self.myl1.config(text='')
            return True

        elif myinp is "":
            print(myinp)
            self.myl1.config(text='')
            return True

        else:
            print(myinp)
            return False

    def myinvalid_name(self, mych):
        self.myl1.config(text=(f'invalid character {mych} \n only numbers are allowed'), font=('Verdana',10))

if __name__ == '__main__':
    myroot = MyValidate()
    myroot.geometry('300x100')
    myroot.mainloop()
