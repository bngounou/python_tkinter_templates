from tkinter import *

myroot = Tk()

myon_img = PhotoImage(width=50, height=25)
myoff_img = PhotoImage(width=50, height=25)

myon_img.put(('lightgreen'), to=(0, 0, 50, 24))
myoff_img.put(('Red'), to=(0, 0, 24, 79))

myrbvar = IntVar(value=1)

myrb1 = Radiobutton(myroot, variable=myrbvar, value=0, bd=0, text="RadioButton1", compound=LEFT, indicatoron=False, image=myoff_img, selectimage=myon_img)
myrb2 = Radiobutton(myroot, variable=myrbvar, value=1, bd=0, text="RadioButton2", compound=LEFT, indicatoron=False, image=myoff_img, selectimage=myon_img)

myrb1.pack(padx=0, pady=0)
myrb2.pack(padx=10, pady=10)

myroot.mainloop()