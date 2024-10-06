# To-Do List Application

# Initialize an empty list to store tasks
todo_list = []

# Function to add a new task to the to-do list
def add_task():
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"\nTask '{task}' has been added to the list.")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, item in enumerate(todo_list, start=1):
            status = "Completed" if item["completed"] else "Pending"
            print(f"{index}. {item['task']} - {status}")

# Function to update an existing task
def update_task():
    view_tasks()
    if not todo_list:
        return
    
    task_number = int(input("\nEnter the task number to update: "))
    
    if 0 < task_number <= len(todo_list):
        new_task = input("Enter the updated task description: ")
        todo_list[task_number - 1]['task'] = new_task
        print(f"\nTask {task_number} has been updated.")
    else:
        print("\nInvalid task number.")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    if not todo_list:
        return
    
    task_number = int(input("\nEnter the task number to mark as completed: "))
    
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]['completed'] = True
        print(f"\nTask {task_number} has been marked as completed.")
    else:
        print("\nInvalid task number.")

# Function to delete a task from the list
def delete_task():
    view_tasks()
    if not todo_list:
        return
    
    task_number = int(input("\nEnter the task number to delete: "))
    
    if 0 < task_number <= len(todo_list):
        deleted_task = todo_list.pop(task_number - 1)
        print(f"\nTask '{deleted_task['task']}' has been deleted.")
    else:
        print("\nInvalid task number.")

# Main program loop
def todo_list_app():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("\nExiting To-Do List application.")
            break
        else:
            print("\nInvalid choice, please try again.")

# Run the to-do list application
todo_list_app()
