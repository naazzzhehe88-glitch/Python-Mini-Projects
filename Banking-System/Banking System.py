account ={ }

if not account:
    print("No accounts found")
 
while True:
    print("""          🏦 Welcome to Naaz Bank
              1.Create Account
              2.Deposit Money
              3.Withdraw Money
              4.Check Balance
              5.Account Details
              6.Show All Accounts
              7.Delete Account
              8.Transfer Money
              9.Show Total Balance in Bank
              10.Exit""")
    
    choice = int(input("Enter your choice : "))
    
    if (choice == 10):
        print("You chose to exit ")
        break

    if (choice == 1):
        name = input("Enter account holder's name: ")
        if name in account:
            print("Account already exists. ")
        else:
            balance = float(input("Enter initial balance: "))
            account[name] = balance
            print("✅ Account created successfully!")
        
    elif (choice==2):
        name = input("Enter account holder's name: ")
        if name in account:
            amount =float(input("Enter amount to deposit: "))
            account[name] = account[name] + amount
            print("✅Money deposited successfully!")
            print(f"Current balance: ₹{account[name]} ")
        else:
            print("No such bank account exists. ")

    elif (choice==3):
        name = input("Enter account holder's name: ")
        if name in account:
            amount = float(input("Enter amount to withdraw: "))

            if (amount<= account[name]):
                account[name] -= amount
                print("💸Withdrew successfully! ")
                print(f"Current Balance: ₹{account[name]}")
            else:
                print("❌Insufficient Balance")
        else:
            print("No such bank account exists. ")

    elif (choice==4):
        name = input("Enter account holder's name: ")
        if name in account:
            print(f"Current Balance: ₹ {account[name]}")
        else:
            print("No such bank account exists")

    elif (choice==5):
         name = input("Enter account holder's name: ")
         if name in account:
             print("======== Account Details ========")
             print("Name: ", name)
             print("Balance: ", account[name])
             print("==================================")

    elif(choice==6):
        for name, balance in account.items():
            print("======== All Accounts ========")
            print("Name: ", name)
            print("Balance: ", balance)
            print("==============================")

    elif(choice==7):
        name = input("Enter account holder's name: ")
        if name in account:
            confirm = input("Are you sure you want to delete this account? (y/n)")
            if confirm.lower()=="y":
                del account[name]
                print("Account deleted.")
            else:
                print("Cancelled")
                
        else:
            print("No such account exists.")
    elif (choice==8):
        sender_name = input("Enter sender's name: ")
        receiver_name = input("Enter receiver's name: ")
        if (sender_name in account and  receiver_name in account):
            amount = float(input("Enter amount to transfer: "))
            if (sender_name ==receiver_name):
                print("You cannot transfer money to yourself.")
            if (amount<=account[sender_name]):
                account[sender_name] -= amount
                account[receiver_name] += amount
                print("👍Transfer successfull")
                
            else:
                print("❌Insufficient Balance")
        else:
            print("One or both the accounts do not exist.")


    elif(choice==9):
        total = 0
        for name, balance in account.items():
            total+=balance
        print(f"Total money in the bank is ₹ {total}")

    else:
        print("Invalid Choice.")

            
