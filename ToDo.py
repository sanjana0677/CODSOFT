tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour Tasks")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. [{status}] {task['name']}")
        print()


while True:
    print("\nTO-DO LIST")
    print("1.View Tasks")
    print("2.Add Task")
    print("3.Update Task")
    print("4.Mark as Completed")
    print("5.Delete Task")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append({"name": task, "done": False})
        print("Task added successfully!")

    elif choice == "3":
        show_tasks()
        if tasks:
            n = int(input("Enter task number: ")) - 1
            if 0 <= n < len(tasks):
                tasks[n]["name"] = input("Enter new task: ")
                print("Task updated successfully!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        show_tasks()
        if tasks:
            n = int(input("Enter task number: ")) - 1
            if 0 <= n < len(tasks):
                tasks[n]["done"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

    elif choice == "5":
        show_tasks()
        if tasks:
            n = int(input("Enter task number: ")) - 1
            if 0 <= n < len(tasks):
                removed = tasks.pop(n)
                print(f'"{removed["name"]}" deleted!')
            else:
                print("Invalid task number!")

    elif choice == "6":
        print("Thank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice! Please try again.")