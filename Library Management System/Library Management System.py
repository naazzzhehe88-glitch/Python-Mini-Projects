library = { }

while True:
    print("""       📖  Library Management System  📖

                1. Add Book
                2. Borrow Book
                3. Return Book
                4. Search Book
                5. Show All Books
                6. Delete Book
                7. Show Total Books
                8. Exit""")
    choice = int(input("Enter your choice: "))
    if (choice==8):
        print("You chose to exit.")
        break
    if (choice==1):
        book = input("Enter the book you want to add: ").title()
        copies = int(input("Enter the number of copies: "))
        if copies <= 0:
            print("Enter a valid number of copies.")
            continue
        if book in library:
            library[book] += copies
            print(f"{copies} copies of '{book}' added to the library.")
        else:
            library[book] = copies
            print(f"'{book}' added to the library with {copies} copies.")

    elif (choice==2):
        book = input("Enter the book you want to borrow: ").title()
        copies = int(input("Enter the number of copies you want to borrow: "))
        if copies <= 0:
            print("Enter a valid number of copies.")
            continue
        if book not in library:
            print("Book is not available in the library.")

        elif library[book] < copies:
            print("Not enough copies available.")

        else:
            if book in library and library[book] >= copies:
                    library[book] -= copies
                    print(f"You have borrowed {copies} copy/copies of '{book}'.")
          

    elif (choice==3):
        book = input("Enter the book you want to return: ").title()
        copies = int(input("Enter the number of copies you want to return: "))
        if copies <= 0:
            print("Enter a valid number of copies.")
            continue
        if book in library:
            library[book] += copies
            print(f"You have returned {copies} copy/copies of '{book}'.")
        else:
            print(f"'{book}' does not belong to this library.")
            ask=input("Do you want to add it to the library? (yes/no)")
            if ask.lower()  == "yes":
                library[book] = copies
                print(f"'{book}' added to the library with {copies} copies.")
            else:
                print("Book not added to the library.")


    elif (choice==4):
        book = input("Enter the book you want to search: ").title()
        if book in library:
            print(f"'{book}' is available with {library[book]} copy/copies.")
        else:
            print(f"'{book}' is not available in the library.")

    elif (choice==5):
        if not library:
            print("Library is empty.")
        else:
            for book,copies in library.items():
                print(f"'{book}' : {copies} copy/copies")

    elif (choice==6):
        book = input("Enter the book you want to delete: ").title()
        
        if book in library:
            confirm = input("Are you sure you want to delete this book? (y/n)")
            if confirm.lower()=="y":
                del library[book]
                print(f"'{book}' has been deleted from the library.")
            else:
                print("Cancelled")
        else:
            print(f"'{book}' is not available in the library.")
        
    elif (choice==7):
        total_books = sum(library.values())
        print(f"Total number of books in the library: {total_books}")

       


    
   