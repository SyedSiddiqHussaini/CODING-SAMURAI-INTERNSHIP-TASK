def task():
    tasks = [] # empty list
    print("----- WELCOME TO THE TASK MANAGEMENT APP ----")

    # Step 1: Initial task setup with error handling
    try:
        total_task = int(input("Enter how many tasks you want to add = "))
        for i in range(1, total_task + 1):
            task_name = input(f"Enter task {i} = ")
            tasks.append(task_name)
    except ValueError:
        print(">> Error: Please enter a valid number for the quantity.")
        return # Exit the function if initial input is wrong

    print(f"\nToday's tasks are: {tasks}")

    # Step 2: Main Menu Loop
    while True:
        print("\n--- OPERATIONS ---")
        print("1-Add  2-Update  3-Delete  4-View  5-Exit")
        
        try:
            operation = int(input("Choose an option (1-5): "))
            
            if operation == 1:
                new_task = input("Enter task you want to add = ")
                tasks.append(new_task)
                print(f"Task '{new_task}' successfully added.")

            elif operation == 2:
                updated_val = input("Enter the task name you want to update = ")
                if updated_val in tasks:
                    new_val = input("Enter new task = ")
                    ind = tasks.index(updated_val) 
                    tasks[ind] = new_val
                    print(f"Updated '{updated_val}' to '{new_val}'")
                else:
                    print(">> Error: Task not found in the list.")

            elif operation == 3:
                del_val = input("Which task you want to delete = ")
                if del_val in tasks:
                    tasks.remove(del_val)
                    print(f"Task '{del_val}' has been deleted.")
                else:
                    print(">> Error: Task not found.")

            elif operation == 4:
                print(f"Current Task List: {tasks}")

            elif operation == 5:
                print("Closing the program. Goodbye!")
                break
            
            else:
                print(">> Error: Please choose a number between 1 and 5.")

        except ValueError:
            print(">> Error: Invalid input! Please enter a number.")

# IMPORTANT: This line calls the function to make it run!
task()