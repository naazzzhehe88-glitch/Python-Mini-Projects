import random

print("Welcome to the game of Rock, Paper and Scissors!")

user_score = 0
computer_score = 0


choice = ["rock", "paper", "scissors"]


win_conditions = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:

    user = input("Enter your choice (Rock/Paper/Scissors) or Quit: ").lower()

    
    if user == "quit":
        print("You chose to quit the game.")
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break


    
    if user not in choice:
        print("Invalid choice! Please choose (Rock/Paper/Scissors) or Quit.")
        continue

    
   

   
    computer_choice = random.choice(choice)
    print("My choice:", computer_choice)

    # game logic
    if user == computer_choice:
        print("Match draw...")

    elif win_conditions[user] == computer_choice:
        print("Congrats! You win!!")
        user_score += 1

    else:
        print("Sorry! You lose!!")
        computer_score += 1

    # score display
    print("Your score:", user_score)
    print("Computer score:", computer_score)

    # play again 
    again = input("Do you want to play again? (yes/no): ").lower()

    if again == "no":
        print("Thank you for playing!")
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break