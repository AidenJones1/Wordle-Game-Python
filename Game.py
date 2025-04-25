import random
import os

# Get the list of words from the file
words = []
try:
    wordFile = open("words.txt", "r")
    words = wordFile.readlines()
    wordFile.close()
except:
    print("Error: words.txt file not found. Please ensure the file is in the same directory as this script.")
    exit()

## Game Loop
while True:
    # Randomly select a word from the list
    wordToGuess = random.choice(words).strip().upper()

    print("Welcome to Wordle!")
    print("You have 5 attempts to guess the 5-letter word.")

    attempts = 0
    playerExited = False

    # Guessing Loop
    while True:
        # User Input
        guess = input("Enter your guess: ").upper()

        # User wishes to exit the game
        if guess == "EXIT":
            print("Thanks for playing!")
            playerExited = True
            break

        # User entered an invalid guess
        if len(guess) != 5 or not guess.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            continue

        # Evaluate the guess
        if guess == wordToGuess:
            print("🟩🟩🟩🟩🟩\nCongratulations! You've guessed the word:", wordToGuess)
            break

        else:
            feedback = ""

            for i in range(5):
                if guess[i] == wordToGuess[i]:
                    feedback += "🟩"
                elif guess[i] in wordToGuess:
                    feedback += "🟨"
                else:
                    feedback += "🟥"

            print(feedback)

        # Iterate attempts
        attempts += 1
        if attempts >= 5:
            print("Sorry, you've used all your attempts. The word was:", wordToGuess)
            break

    # Check if the player exited the game
    if playerExited:
        break

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Starting a new game...")
    else:
        print("Thanks for playing!")
        break