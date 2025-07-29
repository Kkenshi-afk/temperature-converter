tasks=[]
def show_menu():
    print("--------TO DO LIST--------")
    print("1. List Tasks")
    print("2. Add Task")
    print("3.Delete Task")
    print("4. Exit")
def list_task():
    if not tasks:
        print("There are no tasks!")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
def add_task():
    task = input("Type the task you want to add:")
    tasks.append(task)
    print("Task added.")
def delete_task():
    list_task()
    try:
        index = int(input("Type the number of the task you want to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"{deleted} deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter number.")
while True:
    show_menu()
    choice = input("Your choice (1-4): ")

    if choice == '1':
        list_task()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("The program is exiting.")
        break
    else:
        print("Invalid selection.")