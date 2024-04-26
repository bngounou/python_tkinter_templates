from tkinter import *

class MyscrollbarTest(Tk):
    def __init__(self):
        super().__init__()
        mySrollBar1 = Scrollbar(self, orient='horizontal')
        mye1 = Entry(self, xscrollcommand=mySrollBar1.set)
        mye1.focus()
        mye1.pack(side=BOTTOM, fill=X)
        mySrollBar1.pack(fill=X)
        mySrollBar1.config(command=mye1.xview)

if __name__ == "__main__":
    myroot = MyscrollbarTest()
    myroot.geometry('200x200')
    myroot.mainloop()
