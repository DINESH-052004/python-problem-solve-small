tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: "))
        removed = tasks.pop(index - 1)
        print(f"Deleted: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Bye.")
        break
    else:
        print("Invalid choice.")
