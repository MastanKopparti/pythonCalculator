import random
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"
def main():
    print("Welcome to the Rock-Paper-Scissors Game! 🎮")
    user_score = 0
    computer_score = 0
    while True:
        print("\nPlease choose: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        print(f"\nScores:\nYou: {user_score} | Computer: {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break
if __name__ == "__main__":
    main()
