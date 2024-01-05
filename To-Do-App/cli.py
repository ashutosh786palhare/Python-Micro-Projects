import json
import os

# Define the filename for the to-do list data
filename = "todo.json"


def load_data():
    # Check if the file exists
    if not os.path.exists(filename):
        # If it doesn't, create a new file with an empty list
        with open(filename, "w") as file:
            json.dump([], file)

    # Load the data from the file
    with open(filename, "r") as file:
        return json.load(file)


def save_data(data):
    # Save the data to the file
    with open(filename, "w") as file:
        json.dump(data, file)


def display_tasks(tasks):
    # Print the list of tasks
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")


def add_task(tasks, task):
    # Add the new task to the list
    tasks.append(task)


def remove_task(tasks, task_number):
    # Remove the specified task from the list
    del tasks[task_number - 1]


def main():
    while True:
        # Load the tasks from the file
        tasks = load_data()

        # Display the current tasks
        print("\nCurrent Tasks:")
        display_tasks(tasks)

        # Get the user's choice
        print("\nEnter the number of the task you want to perform:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        # Perform the chosen task
        if choice == "1":
            task = input("Enter the task you want to add: ")
            add_task(tasks, task)
            print(f"\nTask '{task}' added successfully.")
        elif choice == "2":
            task_number = int(input("Enter the number of the task you want to remove: "))
            remove_task(tasks, task_number)
            print(f"\nTask {task_number} removed successfully.")
        elif choice == "3":
            pass
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please try again.")

        # Save the tasks to the file
        save_data(tasks)


if __name__ == "__main__":
    main()