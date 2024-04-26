from tkinter import *

class ScrollBar_Entry(Tk):
    def __init__(self):
        super().__init__()

        self.sclhbar = Scrollbar(self, orient=HORIZONTAL)
        self.sclhbar.pack(side=BOTTOM, fill=X)

        self.mye1= Entry(self, xscrollcommand=self.sclhbar.set)
        self.mye1.pack(expand=0, fill=BOTH)

        for loop in range(26):
            self.mye1.insert(END, str(loop) + '\t')
            self.sclhbar.config(command=self.mye1.xview)

if __name__ == '__main__':
    myroot = ScrollBar_Entry()
    myroot.geometry('300x100')
    myroot.mainloop()