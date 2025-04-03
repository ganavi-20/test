def show_tasks(tasks):
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def to_do_list():
    tasks = []

    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. Show Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            tasks.append(task)
        elif choice == '2':
            show_tasks(tasks)
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
            else:
                print("Invalid task number.")
        elif choice == '3':
            show_tasks(tasks)
            task_num = int(input("Enter the task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] = tasks[task_num - 1] + " (Done)"
            else:
                print("Invalid task number.")
        elif choice == '4':
            show_tasks(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

to_do_list()
