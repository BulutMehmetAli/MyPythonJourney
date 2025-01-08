import random
import math

lower = int(input("Enter your range(smaller):"))
upper = int(input("Enter your range(bigger):"))

randomNumber = random.randint(lower,upper)

guessAmount = 0

result = True

#Explanation 1:
while (result!=False):

    guessNumber = int(input("Enter guess number:"))

    if(guessNumber > randomNumber):
        print("Your guess is too high")
        guessAmount+=1
    elif(guessNumber < randomNumber):
        print("Your guess is too small")
        guessAmount+=1
    else:
        print("Congrutulations you guessed it:" , randomNumber )
        guessAmount+=1
        print("Total Number of Guesses = " + str(guessAmount))
        result = False
        


print("****************************************************************************")

# #Explanation 2:

# amountLimit = math.ceil(math.log(upper-lower,2))

# while (result!=False):

#     guessNumber = int(input("Enter guess number:"))

#     if(guessAmount == amountLimit):
#         print("Your came to limit chances.Yo will became succsess nex time !!!")
#         print(f"Guess number is : {guessNumber} but you pass amount of chances : {amountLimit}")
#         result=False
#     if(guessNumber > randomNumber):
#         print("Your guess is too high")
#         guessAmount+=1
#     elif(guessNumber < randomNumber):
#         print("Your guess is too small")
#         guessAmount+=1
#     else:
#         print("Congrutulations you guessed it:" , randomNumber )
#         guessAmount+=1
#         print("Total Number of Guesses = " + str(guessAmount))
#         result = False
        
    