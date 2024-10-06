import random

def get_computer_choice():
    # Computer randomly chooses rock, paper, or scissors
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user_choice, computer_choice):
    # Game logic: Determine the winner based on user and computer choices
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    # Display user and computer choices, and the result
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    while True:
        # Prompt the user to choose rock, paper, or scissors
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose again.")
            continue
        
        # Get the computer's choice
        computer_choice = get_computer_choice()
        
        # Determine the winner
        winner = get_winner(user_choice, computer_choice)
        
        # Display the result
        display_result(user_choice, computer_choice, winner)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        # Display the scores
        print(f"\nCurrent Score: You {user_score} - Computer {computer_score}")
        
        # Ask the user if they want to play another round
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

# Start the game
play_game()


