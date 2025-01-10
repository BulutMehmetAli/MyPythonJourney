import random
import sys

def startGame():
    countList = []
    computerAppend = []
    while True:
        turnChance = input("Enter 'F' to take the first chance.\nEnter 'S' to take the second chance\n").upper()
        if(turnChance == "F"):
            while True:
                    #countList.append(1)
                    print("\nYour turn.")
                    userChoice =int(input("\nHow many numbers do you wish to enter?\n"))
                    if userChoice > 0 and userChoice <= 4:
                        if len(countList) == 0:
                            # Liste boşsa 1'den başlayarak elemanları ekle
                            countList.append(1)
                            for i in range(2, userChoice + 2):
                                countList.append(i)
                        else:
                            # Liste doluysa en büyük elemandan itibaren elemanları ekle
                            
                            start = countList[-1] + 1
                            for i in range(start, start + userChoice):
                                countList.append(i)   
                            if countList[-1] == 20:
                                print("Total List: " , countList).__repr__
                                print("Computer List: " , computerAppend).__repr__
                                print("You winner!!!")
                                print("Computer were losed")
                                sys.exit()                                              
                    else:
                        print ("Wrong input. You are disqualified from the game.")
                        print ("\n\nYOU LOSE !")
                        sys.exit()
                    print("It's time on the computer")
                    computerChoice = random.randint(0,4)
                    secondStart = countList[-1] + 1
                    for j in range(secondStart , secondStart+computerChoice):
                        computerAppend.append(j)
                        countList.append(j)
                        if countList[-1] == 20:
                            print("Total List: " , countList).__repr__
                            print("Computer List: " , computerAppend).__repr__
                            print("You losed!!!")
                            print("Computer is winner !!!")
                            sys.exit()
                    print("Total List: " , countList).__repr__
                    print("Computer List: " , computerAppend).__repr__
        if(turnChance == "S"):
            while True:        
                    print("Computer turn.")
                    randComputerTurn = random.randint(0,4)
                    if len(countList) == 0:
                            countList.append(1)
                            # Liste boşsa 1'den başlayarak elemanları ekle
                            for i in range(2, randComputerTurn + 2):
                                computerAppend.append(i)
                                countList.append(i)
                    else:
                            # Liste doluysa en büyük elemandan itibaren elemanları ekle
                            start3 = countList[-1] + 1
                            for i in range(start3, start3 + randComputerTurn):
                                computerAppend.append(i)
                                countList.append(i)
                            if countList[-1] == 20:
                                print("Total List: " , countList).__repr__
                                print("Computer List: " , computerAppend).__repr__ 
                                print("Computer is winner")
                                print("You losed")
                                sys.exit()      
                    print("Your turn")
                    select2 = int(input("\nHow many numbers do you wish to enter?\n" ))
                    start3 = countList[-1] + 1
                    for i in range(start3 , start3+ select2):
                        countList.append(i)
                        if countList[-1] == 20:
                                print(countList)
                                print("You winer!!!")
                                print("Computer losed !!!")
                                sys.exit()
                    print("Total List: " , countList).__repr__
                    print("Computer List: " , computerAppend).__repr__

startGame()