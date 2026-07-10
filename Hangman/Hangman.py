import random

words = ["Jameson","Avery","Grayson","Nash","Max","Xander","Libby","Hannah","Gigi","Savannah","Rohan","Oren","Toby","Tobias","Alice","Nan","Alisa","Lyra","Tahiti","Prague","Heiress","Riddles","Risk","Secrets","Gamble","Legacy","Win","Mansion","Billionaire","Clues","Tunnels","Reckless","Adrenaline","Perfect","Scones","M.G"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

display = ["_"]*len(word) #keep in mind

print("Welcome to Hangman (The Inheritance Saga)!")
print("*Note the first letter is always capital.")
while wrong_guesses<max_wrong_guesses and "_" in display:
    print("\nWord: ", " ".join(display))
    print(f" Attempts left: {max_wrong_guesses - wrong_guesses}")
    guess=input("Guess a letter: ").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("Enter only one alphabet.")
        continue
    if guess in guessed_letters:
        print("Letter is already guessed.")
        continue
    guessed_letters.append(guess)

    if guess in word:
        for i,letter in enumerate(word):
            if letter==guess:
                display[i]=guess
        print("Correct!")
    else:
        wrong_guesses+=1
        print("Wrong guess!")
if"_" not in display:
    print("You win! The word was: ",word)
else:
    print("You lost! The word was: ",word)
    again = input("Want to play again? (yes/no)").lower
    if 'no':
        print("Thank you for playing")