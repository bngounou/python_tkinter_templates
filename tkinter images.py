from tkinter import *

class MyBtnImage(Frame):
    def __init__(self, root=None):
        Frame.__init__(self,root)
        self.root=root
        self.myphoto = PhotoImage(file='Turtle.png')
        def myclick():
            self.mybtn1['state']=DISABLED
        self.mybtn1 = Button(self.root,image=self.myphoto, command=myclick)
        self.mybtn1.pack(padx=10, pady=10)

if __name__ == '__main__':
    myroot=Tk()
    myobj = MyBtnImage(myroot)
    myroot.title('image using button')
    myroot.geometry('400x400')
    myroot.mainloop()
