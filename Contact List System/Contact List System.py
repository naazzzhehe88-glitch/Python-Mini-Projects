contacts = { }

while True:
    print (""" 
           Contact List System
           1. Add Contacts
           2. View Contacts
           3.Search Contacts
           4. Update Contact
           5. Delete Contact
           6. Exit""")
    choice = int(input("Enter your choice:"))
    
    if (choice == 6):
        print("You chose to exit ")
        break
    if (choice == 1):
    
        name = input( "Enter name :" )
        number =(input("Enter phone number :"))
        if name in contacts:
            print("Contact already exists.")
        else:
            contacts[name]= number

    elif (choice ==2):
        if not contacts:
            print("No contacts found")
        else:
            for name,number in contacts.items():               #
                print(name, ":", number)


    elif(choice==3):
        name = input("Enter name to be searched : ")
        if name in contacts:
            print(contacts[name])

    elif(choice==4):
        name = input ("Which contact to update? ")
        if name in contacts:
            new_number= int(input("Enter new number "))
            contacts[name] = new_number
        else:
           print("No such contact exist ")

    elif(choice==5):
        name=input("Enter contact to delete: ")
        if name in contacts:
            del contacts[name]
        else:
             print("No such contact exist ")
    else:
        print("Invalid choice")
