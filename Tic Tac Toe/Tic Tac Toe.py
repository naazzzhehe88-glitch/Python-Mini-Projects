import random

board = [" "] * 9

winning_combinations = [
    [0, 1, 2],  [3, 4, 5], [6, 7, 8], #rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], #columns
    [0, 4, 8], [2, 4, 6]  #diagonals
]

print("===== TIC TAC TOE =====")

name = input("Enter your name: ")

choice = input("Choose your symbol (X/O): ").upper()

while choice not in ["X", "O"]:
    print("Invalid choice!")
    choice = input("Choose X or O: ").upper()

if choice == "X":
    ai = "O"
else:
    ai = "X"


while True:

    # Print Board
    print()

    for i in range(9):
        if board[i] == " ":
            print(i + 1, end="")
        else:
            print(board[i], end="")

        if i % 3 != 2:
            print(" | ", end="")
        else:
            print()

            if i != 8:
                print("--+---+--")

    print()

    # Player Move
    try:
        position = int(input(f"{name}, choose a position (1-9): ")) - 1
    except ValueError:
        print("Enter numbers only!")
        continue

    if position < 0 or position > 8:
        print("Invalid Position!")
        continue

    if board[position] != " ":
        print("Position already occupied!")
        continue

    board[position] = choice

    # Player Win Check
    player_won = False

    for combo in winning_combinations:

        if (
            board[combo[0]] ==
            board[combo[1]] ==
            board[combo[2]] == choice
        ):
            player_won = True
            break

    if player_won:

        print()

        for i in range(9):
            if board[i] == " ":
                print(i + 1, end="")
            else:
                print(board[i], end="")

            if i % 3 != 2:
                print(" | ", end="")
            else:
                print()

                if i != 8:
                    print("--+---+--")

        print(f"\n🎉 Congratulations {name}! You Won!")
        break

    # Draw Check
    if " " not in board:
        print("It's a Draw!")
        break

    # AI Move

    available = []

    for i in range(9):
        if board[i] == " ":
            available.append(i)

    ai_position = random.choice(available)

    board[ai_position] = ai

    print(f"\nComputer chose position {ai_position + 1}")

    # AI Win Check

    ai_won = False

    for combo in winning_combinations:

        if (
            board[combo[0]] ==
            board[combo[1]] ==
            board[combo[2]] == ai
        ):
            ai_won = True
            break

    if ai_won:

        print()

        for i in range(9):
            if board[i] == " ":
                print(i + 1, end="")
            else:
                print(board[i], end="")

            if i % 3 != 2:
                print(" | ", end="")
            else:
                print()

                if i != 8:
                    print("--+---+--")

        print("\n💻 Computer Wins!")
        break

    # Draw Check Again
    if " " not in board:
        print("It's a Draw!")
        break


print("\nGame Over!")