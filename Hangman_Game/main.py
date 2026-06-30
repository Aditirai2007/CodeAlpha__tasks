import random

# List of words
words = ["engineer", "keyboard", "internet", "college", "algorithm"]

# Choose a random word
word = random.choice(words)

# Create blank spaces
display = ["_"] * len(word)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6  # Standard hangman usually allows 6 wrong guesses

print("====================================")
print("Welcome to Hangman!")
print("====================================")

# Game Loop
while wrong_guesses < max_wrong and "_" in display:
    print(f"\nWord to guess: {' '.join(display)}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    
    guess = input("Guess a letter: ").lower()
    
    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
        
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
        for index, letter in enumerate(word):
            if letter == guess:
                display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        wrong_guesses += 1

# Game Over Conditions
if "_" not in display:
    print(f"\n🎉 Congratulations! You won! The word was: {word}")
else:
    print(f"\n💀 Game Over! You ran out of guesses. The word was: {word}")
