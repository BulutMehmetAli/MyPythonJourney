import random

# Ask the user for their name
name = input("Enter your name: ")
print("Welcome to guess word game", name)

# List of words to be used in the word guessing game
words = ['art', 'elephant', 'mystery', 'ambitious', 'calculator', 
         'submarine', 'jazz', 'extravagant', 'breeze', 
         'algebra', 'innovation', 'volcano', 'whisper', 
         'knight', 'catastrophe']

# Randomly select a word from the list
randomWord = random.choice(words)

# Total number of attempts allowed for the player
userRight = 12

# Variable to store the player's previous guesses
guesses = ''

# Main game loop
while userRight >= 0:

    # Variable to track incorrect guesses
    failed = 0

    # Loop through each character of the randomly selected word
    for char in randomWord:
        # If the character has been guessed, display it
        if char in guesses:
            print(char, end=" ")  # Print the correctly guessed character
        else:
            print("_", end=" ")  # Hide unguessed characters with '_'
            failed += 1  # Increment the count of incorrect guesses

    print()  # Move to the next line

    # If no characters remain hidden, the player wins
    if failed == 0:
        print("You win !!!")
        print("Your guessed word is:", randomWord)
        break  # Exit the loop

    # Ask the user to guess a letter
    guess = input("Enter your guess: ")

    # Add the user's guess to the list of guesses
    guesses += guess

    # If the guessed letter is not in the word
    if guess not in randomWord:
        userRight -= 1  # Decrease the number of remaining attempts
        print("Missed guess")
        print("You have", userRight, "more guesses")
        # If the user runs out of attempts, end the game
        if userRight == 0:
            print("You defeated.")
            print("True word is:", randomWord)
            break