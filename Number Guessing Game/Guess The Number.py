import random

while True:   # OUTER LOOP -> play again

    target = random.randint(1, 100)

    print("Welcome to the Guess the Number Game!")

    # choose difficulty level
    level = input("Choose a difficulty level (Easy, Medium, Hard): ")

    if level == "Easy":
        max_turns = 10
        print("You have chosen Easy difficulty. You have 10 turns to guess the number.")

    elif level == "Medium":
        max_turns = 5
        print("You have chosen Medium difficulty. You have 5 turns to guess the number.")

    elif level == "Hard":
        max_turns = 3
        print("You have chosen Hard difficulty. You have 3 turns to guess the number.")

    elif level == "Quit":
        print("You have chosen to quit the game.")
        break

    else:
        print("Invalid difficulty level. Defaulting to Easy.")
        max_turns = 10
        print("You have 10 turns to guess the number.")

    turns = 0

    while turns < max_turns:   # INNER LOOP -> guessing

        guess = input("Guess the target number between 1 and 100 or Quit: ")

        if guess == "Quit":
            print("You have chosen to quit the game. The target number was:", target)
            break

        guess = int(guess)
        turns += 1
        difference = abs(guess - target)

        if guess == target:
            print("Congratulations! You guessed the correct number:", target)
            print("You took", turns, "turns to guess the number.")
            break

        elif guess < target:
            print("Your guess is too low. Try again.")
            print("Remaining turns:", max_turns - turns)

        else:
            print("Your guess is too high. Try again.")
            print("Remaining turns:", max_turns - turns)

        # hint system works for BOTH high and low guesses
        if difference <= 5:
            print("Hint: You're very close!")
        elif difference <= 10:
            print("Hint: You're close!")
        elif difference <= 20:
            print("Hint: You're not too far.")
        else:
            print("Hint: You're far away.")

    # if user loses
    if turns == max_turns and guess != target:
        print("Sorry, you've reached the maximum number of turns.")
        print("The target number was:", target)

    # play again
    again = input("Do you want to play again? (yes/no): ")

    if again == "no":
        print("Thank you for playing!")
        break