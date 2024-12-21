import random


# Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice, please choose again.")


# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"

    if (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"


# Function to play one round of the game
def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

    return result


# Main function to run the game with multiple rounds
def play_game():
    user_score = 0
    computer_score = 0
    ties = 0

    print("Welcome to Rock, Paper, Scissors!\n")

    while True:
        result = play_round()

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        else:
            ties += 1

        print(f"\nCurrent Score: You: {user_score} | Computer: {computer_score} | Ties: {ties}")

        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            break


# Run the game
if __name__ == "__main__":
    play_game()
