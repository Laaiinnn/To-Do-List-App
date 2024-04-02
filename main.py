class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.description}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_complete()
        else:
            print("Invalid task index")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully")
        else:
            print("Invalid task index")

    def delete_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]
        print("Completed tasks deleted successfully")

    def clear_all_tasks(self):
        self.tasks.clear()
        print("All tasks cleared")


def print_header():
    header = """
 __          __  _                                      
 \ \        / / | |                                      
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/ 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  

         Welcome to the To-Do List App                  
"""
    print(header)


def main():
    print_header()
    todo_list = TodoList()

    while True:
        print("\nMain Menu")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Delete Completed Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)

        elif choice == '2':
            todo_list.view_tasks()
            task_index = int(input("Enter task index to mark as complete: ")) - 1
            todo_list.mark_task_complete(task_index)

        elif choice == '3':
            todo_list.view_tasks()

        elif choice == '4':
            todo_list.view_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)

        elif choice == '5':
            todo_list.delete_completed_tasks()

        elif choice == '6':
            confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
            if confirm == 'y':
                todo_list.clear_all_tasks()

        elif choice == '7':
            print("Exiting the To-Do List App...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
