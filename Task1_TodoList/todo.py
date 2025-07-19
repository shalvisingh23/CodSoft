# Task 1 - To-Do List Application

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def complete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index] += " ✅"
        print("Task completed!")

def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Bye!")
            break
        else:
            print("Invalid option")

main()
