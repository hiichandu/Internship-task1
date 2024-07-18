def main():
    tasks = []

    while True:
        print("\nTasks:")
        print_tasks(tasks)

        print("\nOptions:")
        print("1. Add a task")
        print("2. Complete a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            complete_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def print_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def add_task(tasks):
    task = input("Enter task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")


def complete_task(tasks):
    print_tasks(tasks)
    if tasks:
        index = int(input("Enter the number of the task to complete: ")) - 1
        if 0 <= index < len(tasks):
            completed_task = tasks.pop(index)
            print(f"Task '{completed_task}' completed and removed from the list.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to complete.")


def remove_task(tasks):
    print_tasks(tasks)
    if tasks:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to remove.")


if __name__ == "__main__":
    main()
