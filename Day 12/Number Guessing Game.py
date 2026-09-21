from random import randint
from Number_Guessing_Art import logo

easy_level_turns = 10
hard_level_turns = 5

# Function to check users guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    # Repeat guessing if user is wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != answer:
            print("Guess again.")

game()
