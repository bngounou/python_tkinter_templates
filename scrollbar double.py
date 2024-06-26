from tkinter import *

class DblScrollBar(Tk):
    def __init__(self):
        super().__init__()

        self.myscrlbarv = Scrollbar(self, orient=VERTICAL)
        self.myscrlbarv.pack(side=RIGHT, fill=Y)

        self.myscrlbarh = Scrollbar(self, orient=HORIZONTAL)
        self.myscrlbarh.pack(side=BOTTOM, fill=X)

        self.mytextbox = Text(self, width=500, height=500, yscrollcommand=self.myscrlbarv.set,
                              xscrollcommand=self.myscrlbarh.set, wrap=NONE)
        self.mytextbox.pack(expand=0, fill=BOTH)

        for loop in range(26):
            self.mytextbox.insert(END, str(loop)+ '\t')

        for loop in range(50):
            self.mytextbox.insert(END, str(loop)+ '\n')

        self.myscrlbarh.config(command=self.mytextbox.xview)
        self.myscrlbarv.config(command=self.mytextbox.yview)


if __name__ == '__main__':
    myroot = DblScrollBar()
    myroot.geometry('300x300')
    myroot.mainloop()

"""from tkinter import *
class Scrollbar_Text(Tk):
def __init__(self):
super().__init__()
self.mysclbar = Scrollbar(self)# scrollbar creation and attaching
to the main window
self.mysclbar.pack(side=RIGHT, fill=Y) # scrollbar added to the window right side
self.sclhbar = Scrollbar(self,orient = HORIZONTAL)
self.sclhbar.pack(side = BOTTOM,fill = X)
self.mytxt = Text(self,
width = 600,
height = 600,
yscrollcommand=self.mysclbar.set,
xscrollcommand=self.sclhbar.set,
wrap = NONE) # creation of textbox
and both horizontal and vertical scrollbars are attached
to the textbox
self.mytxt.pack(expand = 0, fill=BOTH)
# horizontal elements
for loop in range(26): # insertelements
from 0 to 49 in the text
self.mytxt.insert(END, str(loop) + '\t')
# vertical elements
for loop in range(50): # insertelements
from 0 to 49 in the text
self.mytxt.insert(END, str(loop) + '\n')
self.sclhbar.config(command=self.mytxt.
xview)# for need of horizontal view settings scrollbar command option
to textbox.xview method
self.mysclbar.config(command=self.mytxt.
yview) # for need of vertical view settings scrollbar command option
to textbox.yview method
if __name__ == '__main__':
myroot = Scrollbar_Text() # creating an instance of Scrollbar_
Text
myroot.geometry('300x300')
myroot.mainloop() # infinite loop to run the application"""