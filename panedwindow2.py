from tkinter import *
myroot = Tk()
myroot.geometry('250x250')

def mynavigate():
    myTopObjet= Toplevel(myroot)
    myTopObjet.geometry('250x250')
    myTopObjet.title('MonTopleve1')

    mylbl1= Label(myTopObjet, text='Ceci est une top Level Window')
    mylbl1.pack(pady=10)

    mybtn1 = Button(myTopObjet, text='ma window top level2', command=func_mytoplevel2)
    mybtn1.pack(pady=10)

    mybtn2 = Button(myTopObjet, text='exit', command=myTopObjet.destroy)
    mybtn2.pack(pady=10)

    myTopObjet.mainloop()


def func_mytoplevel2():
    mytopObject2 = Toplevel(myroot)
    mytopObject2.geometry('250x250')
    mytopObject2.title('Mon top level 2')

    myl1 = Label(mytopObject2, text = 'ceci est une fenêtre top level2')
    myl1.pack(pady=10)

    mybtn2 = Button(mytopObject2, text='exit2', command=mytopObject2.destroy)
    mybtn2.pack(pady=10)
    mytopObject2.mainloop()

mybtn1 = Button(myroot, text = 'my top level1', command=mynavigate)
mybtn1.place(x=100,y=100)
myroot.lift(func_mytoplevel2())

myroot.mainloop()


