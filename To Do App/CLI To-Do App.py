tasks = []

while True:
    print("""
           To-Do List App
           1. Add Task
           2. View Tasks
           3. Remove Task
           4. Exit
          """)

    choice = input("Enter your choice: ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue

    # ADD TASK
    if choice == "1":
        task_name = input("Enter the task name: ")
        tasks.append(task_name)
        print("Task added successfully!")

    # VIEW TASKS
    elif choice == "2":

        # check empty list first
        if not tasks:
            print("No tasks found!")
            continue

        # numbering tasks
        for i, task in enumerate(tasks):
            print(i+1, task)

    # DELETE TASK
    elif choice == "3":

        # check empty list first
        if not tasks:
            print("No tasks to delete!")
            continue

        # show tasks before deleting
        for i, task in enumerate(tasks):
            print(i, task)

        delete = int(input("Enter the task number to delete: "))

        # bounds check
        if 0 <= delete < len(tasks):
            tasks.pop(delete)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")

    # EXIT
    elif choice == "4":
        print("Exiting the To-Do List App. Goodbye!")
        break