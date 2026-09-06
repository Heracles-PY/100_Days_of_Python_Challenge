import random
import nltk

nltk.download("words")
from nltk.corpus import words

import hangman_art

print(hangman_art.logo)

# Filter words to only lowercase, alphabetic entries between 4 and 10 letters
word_list = [
    w.lower()
    for w in words.words()
    if w.isalpha() and w.islower() and 4 <= len(w) <= 10
]

chosen_word = random.choice(word_list)

lives = 6
guessed_letters = set()
game_over = False

print(f"Word to guess: {'_ ' * len(chosen_word)}")

while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").strip().lower()

    # Input validation: enforce exactly one alphabetic character
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter (a-z).")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.add(guess)

    # Check guess against the chosen word
    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word!")
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")
        print(hangman_art.stages[lives])

    # Rebuild and show the board
    display = [letter if letter in guessed_letters else "_" for letter in chosen_word]
    print(f"Word to guess: {' '.join(display)}")

    # Check win/loss conditions
    if "_" not in display:
        game_over = True
        print("\n**************************** YOU WIN! ****************************")
    elif lives == 0:
        game_over = True
        print(f"\nThe correct word was: {chosen_word}")
        print("**************************** YOU LOSE ****************************")
