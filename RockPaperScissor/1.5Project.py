import random

def startGame():
    print("Welcome to Rock-Paper-Scissor Game")
    arrayRandom = [" ","Rock","Paper","Scissor"]
    counter = []
    boolResult = True
    print("1-)Rock\n2-)Paper\n3-)Scissor")
    while (boolResult == True):
        userChoicing = int(input("Enter your choose:"))
        result = ''
        if(userChoicing<0 or userChoicing>3):
            print("You entered wrong value!!!")
        else:
            turnComputer = random.choice(arrayRandom)

            if(turnComputer == "Rock"):
                turnComputer2 = 1
            elif(turnComputer == "Paper"):
                turnComputer2 = 2 
            elif (turnComputer == "Scissor"):
                turnComputer2 = 3

            if (userChoicing == 1 and turnComputer2 == 3) or  (userChoicing == 3 and turnComputer2 == 1):
                result = "Rock"
            elif(userChoicing == 2 and turnComputer2 == 1) or  (userChoicing == 1 and turnComputer2 == 2):
                result = "Paper"
            elif(userChoicing == 3 and turnComputer2 == 2) or  (userChoicing == 2 and turnComputer2 == 3):
                result = "Scissor"
            

            print("You:" , arrayRandom[userChoicing] , "\nComputer:" ,arrayRandom[turnComputer2])
            if arrayRandom[userChoicing] == result:
                print("You winner!!!")
            elif arrayRandom[userChoicing] == arrayRandom[turnComputer2]:
                print("Draw")
            else:
                print("You losed.\nComputer winner!!!")

startGame()