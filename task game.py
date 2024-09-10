import random

def get_computer_choice():
    # Randomly select between rock, paper, or scissors
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # Prompt the user to enter their choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the rules
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_again():
    # Ask the user if they want to play again
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == 'yes'

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\n{result}")

        if not play_again():
            print("Thanks for playing! Goodbye!")
            break

if _name_ == "_main_":
    play_game()
