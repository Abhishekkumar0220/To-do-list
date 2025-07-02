def task():
    tasks = []  # Empty list
    print("----- Welcome To The Task Management App -----")

    total_task = int(input("Enter how many tasks you want to add: "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print("Today's tasks are:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

    # Start operations
    while True:
        print("\nChoose an operation:")
        operation = int(input("1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nEnter your choice: "))

        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task name: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' updated to '{up}'.")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            del_val = input("Enter the task name you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print(f"Task '{del_val}' not found.")

        elif operation == 4:
            if not tasks:
                print("No tasks available.")
            else:
                print("Current tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 5.")

# Call the function to run
task()
