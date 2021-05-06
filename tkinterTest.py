from tkinter import *

top = Tk()
playlist =[]
def results():
    result= E1.get()
    playlist.append(result)
    E1.delete(0,END)

def printList():
    print(playlist)

def exportList():
    with open('test.txt', 'w') as f:
    for item in playList:
        f.write("%s/n" % item)


L1 = Label(top, text="Playlist Generator")

L1.grid(column = 0 , row = 1)

E1 = Entry(top, bd = 7)

E1.grid(column = 0, row = 2)

B1 = Button(text= " Ya like jazzzzz? ", bg="lightgreen", command= results)
B1.grid(column = 1, row = 2)

B2 = Button(text=" Print Playlist ", bg="lightblue", command= printList)
B2.grid(column = 2, row =2)

top.mainloop()
