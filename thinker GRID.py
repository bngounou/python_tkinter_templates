from tkinter import *

myroot =Tk()

mybtn_col = Button(myroot, text="It is column N°4")
mybtn_col.grid(row=0, column=4)

mybtn_colspan = Button(myroot, text="The column span is 4")
mybtn_colspan.grid(row=1, columnspan=4)

mybtn_paddingx = Button(myroot, text="padx of 5 from outside widget border")
mybtn_paddingx.grid(row=2, padx=5, column=2, columnspan=3)

mybtn_paddingy = Button(myroot, text="pady of 5 from outside widget border")
mybtn_paddingy.grid(row=3, pady=5)

mybtn_ipaddingx = Button(myroot, text="ipadx of 5 from inside widget border")
mybtn_ipaddingx.grid(row=4, padx=5)

mybtn_ipaddingy = Button(myroot, text="ipady of 15 from inside widget border")
mybtn_ipaddingy.grid(row=5, ipady=15)

mybtn_row = Button(myroot, text="It is row nb 7")
mybtn_row.grid(row=7, column=2)

mybtn_rowspan = Button(myroot, text="It is a rowspan of 3")
mybtn_rowspan.grid(row=7, rowspan=3)
mybtn_sticky = Button(myroot, text="Hey, I'm from northwest")
mybtn_sticky.grid(sticky=NW)


myroot.mainloop()
