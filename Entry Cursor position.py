from tkinter import *

class MyCursorPosition(Tk):
    def __init__(self):
        super().__init__()
        self.title('My Cursor Position')
        self.mye1 = Entry(self, font="Arial", width=20, bd=5)
        self.mye1.pack(side=LEFT)
        self.mye1.focus()
        self.mye1.insert(0,'demonstration')
        self.mye1.icursor(0)

        self.btn1 = Button(self, text='Position du cursor', command=lambda : myposition(self.mye1))
        self.btn1.pack(pady=32)

        def myposition(mye1):
            mye1.icursor(3)

if __name__ == '__main__':
    myroot = MyCursorPosition()
    myroot.geometry('400x100')
    myroot.mainloop()



