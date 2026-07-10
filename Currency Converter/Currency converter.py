print("""
Currency Converter

1. INR to USD
2. USD to INR
3. INR to EURO
4. EURO to INR
5. Quit
""")

rates = {
    "USD": 94.53,
    "EURO": 107.43
}

while True:

    choice = input("Choose option: ")

    if choice == "5":
        print("Quit")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        continue

    amount = float(input("Enter amount: "))

    if choice == "1":
        usd = amount / rates["USD"]
        print("Amount in USD is:", usd)

    elif choice == "2":
        inr = amount * rates["USD"]
        print("Amount in INR is:", inr)

    elif choice == "3":
        euro = amount / rates["EURO"]
        print("Amount in EURO is:", euro)

    elif choice == "4":
        inr = amount * rates["EURO"]
        print("Amount in INR is:", inr)

    again = input("Convert again? (yes/no): ").lower()

    if again == "no":
        break