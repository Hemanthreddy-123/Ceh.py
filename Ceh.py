import json
import os
from datetime import datetime

# File paths
DATA_FILE = 'tasks.json'
SETTINGS_FILE = 'settings.json'

# Default settings
default_settings = {
    "theme": "default",
    "sort_by": "due_date"
}

# Load user settings
def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
        except:
            print("Error loading settings. Reverting to default.")
    return default_settings

# Save user settings
def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

# Load tasks from file
def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            print("Error loading tasks. Starting fresh.")
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Display task nicely
def display_task(task, index=None):
    info = f"{task['title']} | Due: {task['due_date']} | Priority: {task['priority']} | Tags: {', '.join(task.get('tags', []))}"
    if index is not None:
        print(f"{index + 1}. {info}")
    else:
        print(info)

# Menu System
def main():
    tasks = load_tasks()
    settings = load_settings()

    while True:
        print("\nTask Manager - Theme:", settings['theme'])
        print("1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Change Settings\n6. Exit")
        choice = input("Select an option: ")

        try:
            if choice == '1':
                title = input("Title: ")
                description = input("Description: ")
                due_date = input("Due Date (YYYY-MM-DD): ")
                priority = input("Priority (low/medium/high): ")
                tags = input("Tags (comma-separated): ").split(",")
                tasks.append({
                    "title": title,
                    "description": description,
                    "due_date": due_date,
                    "priority": priority,
                    "tags": tags
                })
                save_tasks(tasks)
                print("Task added!")

            elif choice == '2':
                if not tasks:
                    print("No tasks available.")
                for i, task in enumerate(tasks):
                    display_task(task, i)

            elif choice == '3':
                index = int(input("Enter task number to update: ")) - 1
                if 0 <= index < len(tasks):
                    task = tasks[index]
                    task['title'] = input(f"New Title ({task['title']}): ") or task['title']
                    task['due_date'] = input(f"New Due Date ({task['due_date']}): ") or task['due_date']
                    task['priority'] = input(f"New Priority ({task['priority']}): ") or task['priority']
                    save_tasks(tasks)
                    print("Task updated!")
                else:
                    print("Invalid task number.")

            elif choice == '4':
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    save_tasks(tasks)
                    print("Task deleted!")
                else:
                    print("Invalid task number.")

            elif choice == '5':
                print(f"Current Theme: {settings['theme']}")
                theme = input("Enter new theme (default/dark/light): ")
                if theme:
                    settings['theme'] = theme
                    save_settings(settings)
                    print("Settings updated!")

            elif choice == '6':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print("An error occurred:", str(e))

# Run app
if __name__ == "__main__":
    main()
