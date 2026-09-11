import random

# List of 5 predefined words
words = ["python", "computer", "program", "developer", "keyboard"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
incorrect_guesses = 0

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_attempts:
    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check for repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")

else:
    print("\n💀 Game Over!")
    print("The word was:", word)
