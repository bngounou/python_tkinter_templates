from tkinter import *

myroot = Tk()
myroot.geometry('200x200')

mybtn1 = Radiobutton(myroot, value=1, text='Radio Btn1', selectcolor='green', bg='blue', indicatoron=False)
mybtn2 = Radiobutton(myroot, value=0, text='Radio Btn2',  bg='red', indicatoron=False)
mybtn3 = Radiobutton(myroot, value=2, text='Radio Btn3',  bg='Lightblue', indicatoron=False)

mybtn1.pack(padx=10, pady=10)
mybtn2.pack(padx=10, pady=5)
mybtn3.pack(padx=10, pady=5)

myroot.mainloop()
