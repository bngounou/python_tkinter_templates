from tkinter import *
from tkinter import messagebox
from tkinter import font
#myroot =Tk()

class MyJustify(Tk):
    def __init__(self):
        super().__init__()
        self.title('justify in Button')

        def mycenterjustify():
            messagebox.showinfo('Justify', 'Justify CENTER')

        def myleftjustify():
            messagebox.showinfo('Justify', 'Justify LEFT')

        def myrightjustify():
            messagebox.showinfo('Justify', 'Justify RIGHT')

        mybtn1 = Button(self, text = 'JUSTIFY\nCENTER\nCENTER CENTER',bd=3, relief=GROOVE, font=("Helvetica", 10), width=20, height=3, command=mycenterjustify)
        mybtn1.pack(pady=10, side=BOTTOM)

        mybtn2 = Button(self, text = 'JUSTIFY\nLEFT\nLEFT LEFT', bd=3, relief=GROOVE, font=("Helvetica", 10), justify=LEFT, width=20, height=3, command=myleftjustify)
        mybtn2.pack(pady=10, side=TOP)

        mybtn3 = Button(self, text = 'JUSTIFY\nRIGHT\nRIGHT RIGHT', bd=4, font=("Helvetica", 10), width=20,justify=RIGHT, height=3, command=myrightjustify)
        mybtn3.pack(pady=50, side=RIGHT)

if __name__ == "__main__":
    myroot = MyJustify()
    myroot.geometry('350x350')
    myroot.mainloop()
