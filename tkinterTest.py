from tkinter import *
import random

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
    LMain.grid(column = 0, row = 0)
    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column = 0, row = 1)
    B2Main = Button(text = "Week 2", bg = "white", command = week2)
    B2Main.grid(column= 0, row = 2)
    B3Main = Button(text = "Week 3", bg = "white", command = week3)
    B3Main.grid(column = 0, row = 4)


def week1():
    clearWindow()
    def results():
        result= E1.get()
        playList.append(result)
        E1.delete(0,END)
        L1 = Label(top, text = "Playlist Generator")

    L1.grid(column = 0 , row = 1)

    E1 = Entry(top, bd = 7)

    E1.grid(column = 0, row = 2)

    B1 = Button(text= " Ya like jazzzzz? ", bg = "lightgreen", command = results)
    B1.grid(column = 1, row = 2)

    B2 = Button(text=" = ", bg = "lightblue", command = printList)
    B2.grid(column = 2, row = 2)

    B3 = Button(text = "Export List", bg = "green", command = exportList)
    B3.grid(column = 0, row = 3)

    Bexit = Button (text = "Clear Window", bg = "red", command = mainMenu)
    Bexit.grid(column = 3, row = 3)

def week2():
    clearWindow()
    def rollDice():

        dieType = E1Week2.get()
        rollTimes = E1Week2.get()
        clearWindow()
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randit(1, int(dieType)))

        L4Week2 = label (tip, text= "Here's Your rolls!")
        L4Week2.grid(column= 0, row= 2)

        L5Week2= label(top, text= "{}".format(myRolls))
        L5Week2.grid(column= 0, row=2)
 
        B2Week2= Button(text="Main Menu", bg="yellow", command= mainMenu)
        B2Week2.grid(column=0, row=3)

        B1Week2 = Button(text= "Roll em", bg="yellow", command= mainMenu)
        B1Week2.grid(column= 2,row=4)

        L1Week2 = Label(top, text= "Dice Roller App")
    
def week3():
    clearWindow()
    def numberLists():
        
        myList = []
        unique_list = []
                
        def mainProgram():
            while True:
                try:
                    print("Hey there! Lets work with lists!")
                    print("Choose one of the following options. Type a NUMBER ONLY!")
                    choice = input("""
        1. Add to list,
        2. Add a bunch of numbers,
        3. Return the value at an index position,
        4. Sort list,
        5. Random  Choice,
        6. Linear Search,
        7. Recursive Search
        8. Print Lists,
        9. Find Sum of Numbers,
        10. End Program   """)
                    if choice == "1":
                        addToList()
                    elif choice == "2":
                        addABunch()
                    elif choice == "3":
                        indexValues()
                    elif choice == "4":
                        sortList(myList)
                    elif choice == "5":
                        randomSearch()
                    elif choice == "6":
                        linearSearch()
                    elif choice == "7":
                        binSearch = input("what number are you looking for?   ")
                        recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
                    elif choice == "8":
                        printLists()
                    elif choice == "9":
                        numberSum()                       
                    else:
                        break
                except:
                    print("An error occurred")

        def addToList():
            newItem = input("Please type an intager!   ")
            myList.append(int(newItem))
            print(myList)

        def addABunch():
            print("we're going to add a BUNCH of numbers!")
            numToAdd = input("How many integers do you want to add?   ")
            numRange = input("And how high would you like these numbers to go to?   ")
            for x in range(0,int(numToAdd)):
                myList.append(random.randint(0,int(numRange)))
            print("Your list is now complete!")

        def sortList(myList):
            for x in myList:
                if x not in unique_list:
                    unique_list.append(x)
            unique_list.sort()
            showMe = input("Wanna see you new list? Y/N   ")
            if showMe.lower() == "y":
                print(unique_list)

        def numberSum():
            lst = []
            num = int(input('would you like to add up?   '))
            for x in range(num):
                numbers = int(input('Number   '))
                lst.append(numbers)
                print("The sum of your numbers are   ", sum(lst))

        
        #indexValues()
        #Stored the result of a input function inside indexPos

        #then we force the value stored in indexPos into an integer (using the int() function)
        #and used that variable to find the index position        

        def indexValues():
            indexPos = input("At what index position would you like to look?   ")
            print(myList[int(indexPos)])

        def randomSearch():
            print("Here's a random value form your list!")
            print(myList[random.randint(0, len(myList)-1)])

        def linearSearch():
            print("""We're going to search through the list in the WORST WAY POSSIBLE!
        because i want you to suffer """)
            searchItem = input("What are you looking for? Number-wise?   ")
            for x in range(len(myList)):
               if myList[x] == int(searchItem):
                   print("Your item is at index {}".format(x))
            print(indexCount)
            
        def recursiveBinarySearch(unique_list, low, high, x):
            if high >= low:
                mid = (high + low) // 2

                if unique_list[mid] == x:
                    print("Oh, your just a lucky dude aren't you? Your number is at position {}".format(mid))
                    return mid

                elif unique_list[mid] > x:
                    return recursiveBinarySearch(unique_list, low, mid -1, x)

                else:
                    return recursiveBinarySearch(unique_list, low, mid + 1, high, x)
            else:
                print("Your number isn't here!")
        """
        Asks the user if they want to print the list and what type of list.
        """
        def printLists():
            if len(unique_list) == 0:
                print(myList)
            else:
                whitchOne = input ("Which list? Sorted or un-sorted?   ")
                if whichOne.lower() == "sorted":
                    print(unique_list)
                else:
                    print(myList)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()
