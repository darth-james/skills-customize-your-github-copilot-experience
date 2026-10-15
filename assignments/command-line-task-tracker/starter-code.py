import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks():
    # TODO: Load and return tasks from TASKS_FILE, or return an empty list if it is missing.
    return []


def save_tasks(tasks):
    # TODO: Save the task list to TASKS_FILE as JSON.
    pass


def add_task(tasks, title):
    # TODO: Add a task dictionary with a title and an incomplete status.
    pass


def display_tasks(tasks):
    # TODO: Print each task with its number and completion status.
    # Print a helpful message if the list is empty.
    pass


def complete_task(tasks, task_number):
    # TODO: Mark the numbered task complete and return True, or return False if invalid.
    return False


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Complete a task")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            if title:
                add_task(tasks, title)
                save_tasks(tasks)
            else:
                print("Task title cannot be empty.")
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_number = int(input("Task number to complete: "))
            except ValueError:
                print("Please enter a number.")
                continue

            if complete_task(tasks, task_number):
                save_tasks(tasks)
                print("Task marked complete.")
            else:
                print("That task number does not exist.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
