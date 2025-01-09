import random
from collections import Counter

words = '''cucumber tomato potato carrot onion spinach broccoli cabbage lettuce parsley asparagus zucchini lion 
tiger elephant giraffe kangaroo dolphin penguin flamingo parrot eagle butterfly dragonfly rainbow sunshine 
thunderstorm lightning hurricane tornado mountain valley forest desert ocean glacier'''

convertToList = words.split(' ')
randomWord = random.choice(convertToList)
guesses = ''
limitedChance = len(randomWord) + 3
flag = 0

if __name__ == '__main__':
    print("Game is starting")

    for i in randomWord:
        print('_' , end = ' ')
    print()

    try:
        while(limitedChance != 0 and flag == 0):
            
            print("You have " , limitedChance , "more user rights")
            limitedChance-=1

            guess = str(input("Enter your guessed character:"))

            if not guess.isalpha():
                print("Enter only  LETTER")
                continue
            elif len(guess)>1:
                print("Enter only a Letter")
                continue
            elif guess in guesses:
                print("You have entered already this character")
                continue

            if guess in randomWord:
                k = randomWord.count(guesses)
                for _ in range(k):
                    guesses+=guess

            for char in randomWord:
                if ((char in guesses) and (Counter(randomWord) != Counter(guesses))):
                    print(char , end= ' ')
                elif Counter(randomWord) == Counter(guesses):
                    print()
                    flag=1
                    break
                else:
                    print('_' , end = ' ')
        print()
        if limitedChance<=0 and Counter(guesses) != Counter(randomWord):
            print("You defeated.")
            print("True word is:" , randomWord)









    except Exception as e:
        print(f'{e}')
