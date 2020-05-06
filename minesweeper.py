from random import *
mat1 = []
mat2 = []

def makemat(lengthOfBoard): #6 pts
#This function takes as an input parameter a number and modifies both mat1 and mat 2
    #so that they are lists of lists (matrices). Mat1 should be a list, with x lists in
    #it. Each of the lists in the list should consist of x 0’s. Mat2 should be a list,
    #with x lists in it. Each of the lists in the list should consist of x ‘-‘s. It
    #returns nothing.
    for x in range(0, lengthOfBoard):
        list1 = []
        list2 = []
        for y in range(0, lengthOfBoard):
            list1.append(0)
            list2.append('-')
        mat1.append(list1)
        mat2.append(list2)
        
def printmat(mat): #6 pts
#This function takes as an input parameter a matrix (either mat1 or mat2 in this case)
    #and prints it out. Note that each row should be on a separate line, but the row
    #itself should be printed on one line, using end = “ “. Another note – to make it look
    #nice and neat I used the “\t” to print out a tab. So, for instance, my print
    #statement might look like this:
    #print top y axis nums
    print('\n')
    for num in range(0, len(mat)):
        print("\t" + str(num), end = "")
    print('\n\n')
    for x in range(0,len(mat)):
        print(str(x) + "\t", end="")
        for y in range(0, len(mat[x])):
            print(str(mat[x][y]) + "\t", end="")
        print('\n')
    print('\n--------------------------------------------------------------------------------\n')

def addStuffToBoard(z, typeOfItem):
    if typeOfItem.upper() == 'B':
        for i in range(0, z):
            while True:
                bombLocationX = randrange(0,len(mat1))
                bombLocationY = randrange(0,len(mat1))
                if str(mat1[bombLocationX][bombLocationY]) == 'b' or str(mat1[bombLocationX][bombLocationY]) == 'a' or str(mat1[bombLocationX][bombLocationY]) == 'g':
                    #do nothing / pick new location
                    print()
                else:
                    mat1[bombLocationX][bombLocationY] = 'b'
                    break
    elif typeOfItem.upper() == 'A':
        for i in range(0, z):
            while True:
                armorLocationX = randrange(0,len(mat1))
                armorLocationY = randrange(0,len(mat1))
                if str(mat1[armorLocationX][armorLocationY]) == 'b' or str(mat1[armorLocationX][armorLocationY]) == 'a' or str(mat1[armorLocationX][armorLocationY]) == 'g':
                    #do nothing / pick new location
                    print()
                else:
                    mat1[armorLocationX][armorLocationY] = 'a'
                    break
    elif typeOfItem.upper() == 'G':
        for i in range(0, z):
            while True:
                goldLocationX = randrange(0,len(mat1))
                goldLocationY = randrange(0,len(mat1))
                if str(mat1[goldLocationX][goldLocationY]) == 'b' or str(mat1[goldLocationX][goldLocationY]) == 'a' or str(mat1[goldLocationX][goldLocationY]) == 'g':
                    #do nothing / pick new location
                    print()
                else:
                    mat1[goldLocationX][goldLocationY] = 'g'
                    break
        
def addscores():
    #check for bomb, gold, or armor below
    for r in range(0,len(mat1)-1):
        for c in range(0, len(mat1)):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r+1][c] == 'a':
                    mat1[r][c] += 100
                elif mat1[r+1][c] == 'g':
                    mat1[r][c] += 10
                elif mat1[r+1][c] == 'b':
                    mat1[r][c] += 1
                 
    #checks for bomb above
    for r in range(1,len(mat1)):
        for c in range(0, len(mat1)):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r-1][c] == 'a':
                    mat1[r][c] += 100
                elif mat1[r-1][c] == 'g':
                    mat1[r][c] += 10
                elif mat1[r-1][c] == 'b':
                    mat1[r][c] += 1

    #checks for bomb to the right
    for r in range(0,len(mat1)):
        for c in range(0, len(mat1)-1):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r][c+1] == 'a':
                    mat1[r][c] += 100
                elif mat1[r][c+1] == 'g':
                    mat1[r][c] += 10
                elif mat1[r][c+1] == 'b':
                    mat1[r][c] += 1

    #checks for bomb to the left
    for r in range(0,len(mat1)):
        for c in range(1, len(mat1)):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r][c-1] == 'a':
                    mat1[r][c] += 100
                elif mat1[r][c-1] == 'g':
                    mat1[r][c] += 10
                elif mat1[r][c-1] == 'b':
                    mat1[r][c] += 1

    #checks for bomb to top right diagonal
    for r in range(1,len(mat1)):
        for c in range(0, len(mat1)-1):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r-1][c+1] == 'a':
                    mat1[r][c] += 100
                elif mat1[r-1][c+1] == 'g':
                    mat1[r][c] += 10
                elif mat1[r-1][c+1] == 'b':
                    mat1[r][c] += 1

    #checks for bomb to top left diagonal
    for r in range(1,len(mat1)):
        for c in range(1, len(mat1)):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r-1][c-1] == 'a':
                    mat1[r][c] += 100
                elif mat1[r-1][c-1] == 'g':
                    mat1[r][c] += 10
                elif mat1[r-1][c-1] == 'b':
                    mat1[r][c] += 1

    #checks for bomb to bottom left diagonal
    for r in range(0,len(mat1)-1):
        for c in range(1, len(mat1)):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r+1][c-1] == 'a':
                    mat1[r][c] += 100
                elif mat1[r+1][c-1] == 'g':
                    mat1[r][c] += 10
                elif mat1[r+1][c-1] == 'b':
                    mat1[r][c] += 1

    #checks for bomb to bottom right diagonal
    for r in range(0,len(mat1)-1):
        for c in range(0, len(mat1)-1):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r+1][c+1] == 'a':
                    mat1[r][c] += 100
                elif mat1[r+1][c+1] == 'g':
                    mat1[r][c] += 10
                elif mat1[r+1][c+1] == 'b':
                    mat1[r][c] += 1

    #Adds zeros
    for r in range(0,len(mat1)):
        for c in range(0, len(mat1)):
            if mat1[r][c] != 'b' and mat1[r][c] != 'g' and mat1[r][c] != 'a':
                if mat1[r][c] < 10:
                    mat1[r][c] = '00' + str(mat1[r][c])
                elif mat1[r][c] < 100:
                    mat1[r][c] = '0' + str(mat1[r][c])
                    
def getsquare(Ac):
    outOfRange = True
    alreadyChosen = True
    while outOfRange == True:
        outOfRange = False
        print('\n')
        print("Enter the cordinates to reveal a spot on the board!")
        #Doing it backwards b/c so that x can be cols and y can be rows 
        y = int(input("Input x: "))
        x = int(input("Input y: "))
        if x < 0 or y < 0 or x > len(mat1)-1 or y > len(mat1)-1:
            print("Value out of bounds, go again.")
            outOfRange = True
        #if space not already chosen
        #alreadyChosen = False
    
    mat2[x][y] = mat1[x][y] #reveals chosen square from hidden board
    if mat2[x][y] == 'b':
        goldIncrease = randrange(0,2)
        if goldIncrease == 1:
            Ac[1] += 20
        bombDmg = randrange(10,50)
        if bombDmg < Ac[0]:
            Ac[0] -= bombDmg
            printmat(mat2)
            print("You hit a bomb dealing: " + str(bombDmg) + " Dmg")
            print("Armor is reduced to: " + str(Ac[0]))
            return True
        else:
            printmat(mat2)
            print("You hit a bomb dealing: " + str(bombDmg) + " Dmg")
            print("You only had: " + str(Ac[0]) + " Armor and therefor, died!")
            return False
    elif mat2[x][y] == 'g':
        newGold = randrange(10,30)
        Ac[1] += newGold
        printmat(mat2)
        print("You found: " + str(newGold) + " Gold")
        print("You have: " + str(Ac[1]) + " Gold")
        return True
    elif mat2[x][y] == 'a':
        newArmor = randrange(10,30)
        Ac[0] += newArmor
        printmat(mat2)
        print("You found: " + str(newArmor) + " Armor")
        print("You have: " + str(Ac[0]) + " Armor")
        return True
    else:
        printmat(mat2)
        return True

def countbombs():
    count = 0
    for r in range(0,len(mat1)):
        for c in range(0, len(mat1)):
            if mat2[r][c] == 'b' or mat2[r][c] == 'F':
                count += 1
    return count
    
def addflag(AddorRemove):
    #add = true
    print('\n')
    if AddorRemove == True:
        print("Enter the cordinates for your flag!")
        #Doing it backwards b/c so that x can be cols and y can be rows
        y = int(input("Input x: "))
        x = int(input("Input y: "))
        mat2[x][y] = 'F'
        printmat(mat2)
        return 1
    else:
        print("Enter the cordinates of the flag you wish to remove!")
        #Doing it backwards b/c so that x can be cols and y can be rows
        y = int(input("Input x: "))
        x = int(input("Input y: "))
        if mat2[x][y] == 'F':
            mat2[x][y] = '-'
            printmat(mat2)
            return -1
        else:
            print("There is no flag at that location!")
        

def ckflags():
    #if all bombs flagged - you win; else - you lose?
    
    for x in range(0, len(mat1)):
        for y in range(0, len(mat1)):
            if mat1[x][y] == 'b' and mat2[x][y] != 'F':
                print("Sorry, you did not flag all of the bombs correctly and have LOST!")
                return False
    return True

def printrules():
     print("""The Goal is to find all the bombs and to gather
     enough gold to buy your way off the board. \n
     You must select a square. The square may contain
     Gold ('G'), Armor ('A'), or a Bomb ('B'). If not,
     it will contain a set of numbers, with the first
     being the number of armor, the second being the
     number of gold squares, and the third being the
     number of bomb squares surrounding that square. \n
     So, for instance, if a Square holds the number 310
     that means it has 3 armors in surrounding squares,
     1 gold in surrounding squares, and no bombs in any
     of the surrounding squares.\n
     When you land on an Armor, your Armor amount increases
     by a random amount between 10 and 30 (including 30).
     If you land on a Bomb, the bomb may have destructive
     power anywhere between 10 and 50. If you are lucky
     enough to have more Armor than bomb strength, you will
     live, but your Armor will be deleted by the amount of
     the bomb. If you don't, you die and the game ends.
     If you land on a bomb, and survive, you may gain 20
     gold points. (or you may not - it's random too.)
     Finally, at any point, you can check to see if you've
     won. You win when you've identified all the bombs
     (either by flagging them or by detonating them)and
     you have collected over 150 Gold nuggets.\n
     As you play, you have a number of options, includng 
     seeing the score of a particular square. This is
     especially useful with squares with gold, bombs, or
     armor in them.""")
     print('\n')

def playgame(totalbombs, TotalGold):
    alive = True
    foundbombs = 0
    Ac = [0,0]
    while(alive):
        x = input("""
            Input:\n
            \t'a' Choose Square:
            \t'b' Add Flag:
            \t'c' Remove Flag:
            \t'd' See Board so Far:
            \t'e' Number of Bombs Left:
            \t'f' See Armor Score:
            \t'g' See Amount of Gold:
            \t'h' Get score for Square:
            \t'i' See Rules of Game:
            \t'q' Quit:
            """)
    
        if x == 'a':
            alive = getsquare(Ac)
        elif x == 'b':
            addflag(True)
            foundbombs = countbombs()
            if foundbombs == totalbombs:
                x = input("Want to check if you are right? (yes or no) **Note weird bug - please enter yes twice!: ")
                if x.upper == "YES":
                    x.ckflags()
                    if (x and (Ac[1] - TotalGold) >= 0):
                        print("You Win! Congratulations!")
                        break
                    elif x:
                        print("Sorry, not enough gold with " + str(Ac[1]))
                        break
                    else:
                        print("You lose!")
                    print("Game Over!")
                    alive = False
                    break
        elif x == 'c':
            addflag(False)
            foundbombs = countbombs()
        elif x == 'd':
            printmat(mat2)
        elif x == 'e':
            print("Your bombs left to find are: " + str(totalbombs - foundbombs) + '\n')
        elif x == 'f':
            print("Your Armor is: " + str(Ac[0]))
        elif x == 'g':
            print("Your Gold is: " + str(Ac[1]))
        elif x == 'h':
            getScore()
        elif x == 'i':
            printrules()
        elif x == 'q':
            print("Game over!")
            alive = False
        else:
            foundbombs = countbombs()
            if foundbombs == totalbombs:
                x = ckflags()
                if (x and (Ac[1] - TotalGold) >= 0):
                    print("You Win! Congratulations!")
                elif x:
                    print("Sorry, not enough gold with " + str(Ac[1]))
                else:
                    print("You Lose!")
            print("Game over!")
            alive = False
        print()

def main():
    printrules()
    difficulty = input("Do you want an easy ('E'), medium ('M'), or hard ('H') board? ")
    if difficulty.upper() == 'E':
        sizeb = 8
        totalbombs = 9
    elif difficulty.upper() == 'M':
        sizeb = 14
        totalbombs = 15
    elif difficulty.upper() == 'H':
        sizeb = 20
        totalbombs = 21
    makemat(sizeb)
    addStuffToBoard(totalbombs, 'B')
    addStuffToBoard(totalbombs, 'A')
    addStuffToBoard(totalbombs, 'G')
    TotalGold = randrange(100,200)
    
    #printmat(mat1)
    printmat(mat2)
    addscores()
    #printmat(mat1)
    
    playgame(totalbombs, TotalGold)

main()
