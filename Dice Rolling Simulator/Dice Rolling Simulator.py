import random
print("Dice Rolling Simulator ")
while True:
    turns = input ("Type 'roll' to roll the dice or 'quit' to exit: ").lower()
    if turns=="quit":
      print("You chose to quit")
      break
    times =int(input ("How many dice to roll?(1 or 2)"))
    if times == 1 :
      number = random.randint(1,6)
      print("🎲 You rolled : ",number)
      
    elif times ==2 :
       total = 0
       number1= random.randint(1,6)
       number2 = random.randint(1,6)
       total = number1 + number2 
       
    else:
       print("Please choose only 1 or 2 dice")
    again = input("Roll again ?(yes/no) ").lower()
    if again=="no":
       print("Thank you for playing.")
       break
