from tkinter import *

top = Tk()
playList = []

def printList():
    print(playList)

def exportList():
    with open('playList.txt', 'w') as f:
        for item in playList:
            f.write("%s/n" % item)

def clearWindow():
    for children in top.winfo_children():
        children.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Progects:")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column = 0, row = 2)
    B2Main = Button(text = "Week 2", bg = "white")
    B2Main.grid(column= 0, row = 2)
    B3Main = Button(text = "Week 3", bg = "white")
    B3Main.grid(column = 0, row = 4)


def week1():
    clearWindow()
    def results():
        result= E1.get()
        playList.append(result)
        E1.delete(0,END)
        L1 = Label(top, text="Playlist Generator")

    L1.grid(column = 0 , row = 1)

    E1 = Entry(top, bd = 7)

    E1.grid(column = 0, row = 2)

    B1 = Button(text= " Ya like jazzzzz? ", bg = "lightgreen", command= results)
    B1.grid(column = 1, row = 2)

    B2 = Button(text=" = ", bg = "lightblue", command= printList)
    B2.grid(column = 2, row = 2)

    B3 = Button(text = "Export List", bg = "green", command = exportList)
    B3.grid(column = 0, row = 3)

    Bexit = Button (text = "Clear Window", bg = "red", command = mainMenu)
    Bexit.grid(column = 3, row = 2)

def week2():
    clearWindow()
    B1Week2 = Button()
    L1Week2 = Label()
    L2Week2 = Label()
    L3Week2 = Label()
    E1Week2 = Entry()
    E2Week2 = Entry()





if __name__ == "__main__":
    mainMenu()
    top.mainloop()
