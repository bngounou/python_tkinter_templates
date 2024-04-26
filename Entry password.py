from tkinter import *

class MyLogin:
    def __init__(self,myroot):
        self.ml1 = Label(myroot, text='username')
        self.ml1.grid(row=0, column=0)

        self.ml2 = Label(myroot, text='password')
        self.ml2.grid(row=1, column=0, padx=10)

        self.myE1 = Entry(myroot, width=15, selectborderwidth=3)
        self.myE1.grid(row=0, column=1)


        self.myE2 = Entry(myroot, width=15, show="*")
        self.myE2.grid(row=1, column=1, pady=10)
        self.myE2.focus()

        def mydislay():
            print("The username is: ",self.myE1.get())
            print("The password is :", self.myE2.get())

        self.mybtn = Button(myroot, text="login", command=mydislay, font=("Arial", 12))
        self.mybtn.grid(row=3, columnspan=2, padx=20)

if __name__ == '__main__':
    myroot = Tk()
    myobj = MyLogin(myroot)
    myroot.title('Login Page')
    myroot.geometry('200x150')
    myroot.mainloop()
