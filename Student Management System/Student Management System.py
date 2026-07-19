students = { }




while True:
    print("""          🎓 Welcome to Student Management System
                1. Add Student
                2. Update Student
                3. Search Student
                4. Delete Student
                5. Show All Students
                6. Show Topper
                7. Show Average Marks
                8. Exit""")
    
    choice = input("Enter your choice: ")

    if choice == "8":
        print("You have exited the Student Management System.")
        break

    elif choice == "1":
        
        name = input("Enter student name: ").title()
        if name in students:
            print("Student already exists.")
            continue
        age = int(input("Enter student age: "))

        subjects = {}
        number = int(input("How many subjects? "))
        if number<=0:
            print("Number of subjects must be greater than 0.")
            continue
        for i in range(number):
            subject = input("Enter subject name: ").title()

            while True:
                marks = int(input("Enter marks: "))

                if 0 <= marks <= 100:
                    break

                print("Marks must be between 0 and 100.")

            subjects[subject] = marks

        students[name] = {"Age": age, "Subjects": subjects}
        print(f"\n{name} has been added successfully!")
    
    elif choice == "2":
        name = input("Enter student name to update:").title()
        if name not in students:
            print("Student not found.")
            continue
        else:
            print("What do you want to update?")
            print("1. Age")
            print("2. Subjects")
            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                new_age = int(input("Enter new age: "))
                students[name]["Age"] = new_age
                print(f"{name}'s age has been updated to {new_age}.")

            elif update_choice == "2":
                print("Current subjects and marks:")
                for subject,marks in students[name]["Subjects"].items():
                    print(f"{subject} : {marks}")
                   
                update_subject = input("Enter subject name to update: ").title()
                if update_subject not in students[name]["Subjects"]:
                    print("Subject not found.")
                    continue
                while True:
                    new_marks = int(input("Enter new marks: "))

                    if 0 <= new_marks <= 100:
                        break

                    print("Marks must be between 0 and 100.")

                students[name]["Subjects"][update_subject] = new_marks
                print(f"{name}'s marks for {update_subject} have been updated to {new_marks}. ")
    elif choice == "3":
        name = input("Enter student name to search: ").title()
        if name not in students:
            print("Student not found.")
            continue
        else:
            print(f"Name: {name}")
            print(f"Age: {students[name]['Age']}")
            print("Subjects and Marks:")
            for subjects, marks in students[name]["Subjects"].items():
                print(f"{subjects} : {marks}")
            total = sum(students[name]["Subjects"].values())
            average = total / len(students[name]["Subjects"])

            print(f"Average Marks : {average:.2f}")

    elif choice == "4":
        name = input("Enter student name to delete: ").title()
        if name not in students:
            print("Student not found.")
            continue
        else:
            confirm = input("Are you sure? (y/n): ")

            if confirm.lower() == "y":
                del students[name]
                print(f"{name} has been deleted from the system.")
            else:
                print("Deletion cancelled.")
           
    

    elif choice == "5":
        if not students:
            print("No students found.")
            continue
        else:
            print("All students: ")
            for name,details in students.items():
                print("-" * 35)
                print(f"Name : {name}")
                print(f"Age  : {details['Age']}")

                print("Subjects:")
                for subject, marks in details["Subjects"].items():
                    print(f"   {subject:<15} {marks}")

                average = sum(details["Subjects"].values()) / len(details["Subjects"])
                print(f"Average : {average:.2f}")

    elif choice == "6":
        if not students:
            print("No students found.")
            continue
        else:
            topper= ""
            highest_average = 0
            for name,details in students.items():
                total_marks = sum(details["Subjects"].values())
                average_marks = total_marks / len(details["Subjects"])
              
                if average_marks> highest_average:
                    highest_average = average_marks
                    topper = name
            print("\n🏆 Topper Details")
            print(f"Name            : {topper}")
            print(f"Average Marks   : {highest_average:.2f}")

            print("Subjects:")
            for subject, marks in students[topper]["Subjects"].items():
                print(f"   {subject:<15} {marks}")          
                                                                                                    
    elif choice == "7":
        if not students:
            print("No students found.")
            continue
        else:
            total_marks = 0
            total_subjects = 0
            for details in students.values():
                total_marks += sum(details["Subjects"].values())
                total_subjects += len(details["Subjects"])
            average_marks = total_marks / total_subjects
            print(f"The average marks of all students is {average_marks:.2f}.")
    
           

       
        
    

