todo_list = []
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            status = "✔️ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['task']} [{status}]")
def add_task():
    task = input("Enter new task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added!")
def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed = todo_list.pop(task_num)
            print(f"Removed: {removed['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please select from 1 to 5.")
