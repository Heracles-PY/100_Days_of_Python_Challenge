import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice: ").lower()
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Would you like to play again? (y/n)").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
    else:
        print("-" * 40)
        continue