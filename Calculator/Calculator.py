def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    return a/b


while True:
    print("""
Calculator
      1.Add
      2. Subtract
      3. Multiply
      4. Divide
      5. Exit
""")
    choice = int(input("Choose option: "))
    if choice==5:
        print ("You choose to exit.")
        break
    
    if choice == 4:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        print(divide(num1,num2))
        continue
    
    if choice==1:
        total = 0
        count = int(input("How many numbers you want to add? "))
        for i in range(count):
            num = float(input("Enter number : "))
            total+=num
        print(total)
    elif choice == 2:
        total = 0
        count = int(input("How many numbers you want to subtract? "))
        for i in range(count):
            num = float(input("Enter number : "))
            total-=num
        print(total)
        
    elif choice == 3:
        total = 1
        count = int(input("How many numbers you want to multiply? "))
        for i in range(count):
            num = float(input("Enter number : "))
            total*=num
        print (total)
    
    else:
        print("Invalid choice")
        
