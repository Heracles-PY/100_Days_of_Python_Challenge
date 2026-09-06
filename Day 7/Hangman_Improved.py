import random
import nltk
nltk.download('words')
from nltk.corpus import words

import hangman_art
print(hangman_art.logo)

word_list = words.words()

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []
guessed_letters = []
lives = 6

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")

    if guess in guessed_letters:
        print(f"You've already guessed {guess}.")
    else:
        guessed_letters.append(guess)
        if guess in chosen_word:
            print(f"Good guess! {guess} is in the word!")
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            print(hangman_art.stages[lives])

    if lives == 0:
        game_over = True
        print(f"The correct word was: {chosen_word}")
        print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
