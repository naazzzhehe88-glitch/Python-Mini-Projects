expenses = []

while True:
    print("""
        💰 Expense Tracker

    1. Add Expense
    2. View All Expenses
    3. Search by Category
    4. Show Total Expenses
    5. Show Highest Expense
    6. Delete Expense
    7. Exit
    """)
     
    choice = input("Enter your choice: ")

    if choice == "7":
        print("Exiting the Expense Tracker. Goodbye!")
        break

    elif choice == "1":
        title = input("Enter the title of the expense:").title()
        category = input("Enter the category of the expense:").title()
        amount = float(input("Enter the amount of the expense:"))
        if amount < 0:
            print("Amount cannot be negative. Please enter a valid amount.")
            continue

        expenses.append({"Title" : title, "Category" : category, "Amount" : amount})
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("All Expenses:")
            for expense in expenses:
                print("-" * 30)
                print(f"Title: {expense['Title']}, Category: {expense['Category']}, Amount: {expense['Amount']:.2f}")
                print("-" * 30)

    elif choice == "3":
        search_category = input("Enter the category to search for:").title()

        for expense in expenses:
            if expense["Category"] == search_category:
                print("-" * 30)
                print(f"Title: {expense['Title']}, Category: {expense['Category']}, Amount: {expense['Amount']:.2f}")
                print("-" * 30)

            else:
                print(f"No expenses found in the category '{search_category}'.")
    
    elif choice == "4":
        total_expenses = sum(expense["Amount"] for expense in expenses)
        print(f"Total Expenses: {total_expenses:.2f}")

    elif choice == "5":
        if not expenses:
            print("No expenses recorded yet.")
        else:
           highest_expense = expenses[0]
           for expense in expenses:
                if expense["Amount"] > highest_expense["Amount"]:
                   highest_expense = expense

                print("-" * 30)

                print("\n💰 Highest Expense")
                print(f"Title    : {highest_expense['Title']}")
                print(f"Category : {highest_expense['Category']}")
                print(f"Amount   : ₹{highest_expense['Amount']:.2f}")

                print("-" * 30)

    elif choice == "6":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            title = input("Enter expense title to delete: ").title()
            for expense in expenses:
                if expense["Title"]== title:
                    confirm = input(f"Are you sure you want to delete the expense '{title}'? (yes/no): ").lower()
                    if confirm == "yes":
                        expenses.remove(expense)
                        print(f"Expense '{title}' deleted successfully.")
                    else:
                        print("Deletion canceled.")

    else:
        print("Invalid choice. Please try again.")
                    