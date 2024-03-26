import random

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "Congratulations! You win!"
    else:
        return "Sorry, you lose."

# Function to play the game
def play_game():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Choose 'rock', 'paper', or 'scissors'. To quit, type 'quit'.")
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("Enter your choice: ").lower()
        if user_choice == 'quit':
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
    
    print("Thanks for playing!")

# Entry point of the program
if __name__ == "__main__":
    play_game()

