from tkinter import *

top = Tk()

def results():
    result= E1.get()
    print(result)
    print(type(result))

L1 = Label(top, text="Hello, world!")

L1.grid(column = 0 , row = 1)

E1 = Entry(top, bd = 7)

E1.grid(column = 0, row = 2)

B1 = Button(text= "    Get Data boiii    ", bg="lightblue", command= resultss)
B1.grid(column = 0, row = 3)

top.mainloop()
