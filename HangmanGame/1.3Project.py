import random
from collections import Counter

words = '''cucumber tomato potato carrot onion spinach broccoli cabbage lettuce parsley asparagus zucchini lion 
tiger elephant giraffe kangaroo dolphin penguin flamingo parrot eagle butterfly dragonfly rainbow sunshine 
thunderstorm lightning hurricane tornado mountain valley forest desert ocean glacier'''

convertToWords = words.split(' ')
randomWord = random.choice(convertToWords)



guesses = ''
flag = 0
limitedChance = len(randomWord)+3

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in randomWord:
        print('_' , end = ' ')
    print()

    try:
        while((limitedChance !=0)  and  (flag==0)):
            
            
            print("You have " , limitedChance , "amount of chance")
            limitedChance-=1
            guess = str(input("Enter your guess character:"))
            
            if not guess.isalpha():
                print("Enter only a LETTER!!!")
                continue
            elif len(guess)>1:
                print("Enter only one letter")
                continue
            elif guess in guesses:
                print("You have already entered this character")

            if guess in randomWord:
                k = randomWord.count(guess)
                for _ in range(k):
                    guesses+=guess

            
            for char in randomWord:
                if (char in guesses) and Counter(randomWord) != Counter(guesses):
                    print(char , end = ' ')
                elif Counter(randomWord) == Counter(guesses):
                    print("You winnn !!!")
                    print("Your word is : " , randomWord)
                    flag = 1
                    break
                    break
                else:
                    print('_' , end= ' ')
        print()
        if limitedChance<=0  and Counter(guesses) != Counter(randomWord):
            print("You done !!! ")                
            print("Right word is :" , randomWord)
    except Exception as e:
        print(f'{e}')
