from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def edit_task(self, task_num, new_task):
        if not self.tasks:
            print("No tasks added yet.")
        elif task_num > len(self.tasks) or task_num < 1:
            print("Invalid task number.")
        else:
            self.tasks[task_num - 1] = new_task

    def delete_task(self, task_num):
        if not self.tasks:
            print("No tasks added yet.")
        elif task_num > len(self.tasks) or task_num < 1:
            print("Invalid task number.")
        else:
            del self.tasks[task_num - 1]

    def set_deadline(self, task_num, deadline):
        if not self.tasks:
            print("No tasks added yet.")
        elif task_num > len(self.tasks) or task_num < 1:
            print("Invalid task number.")
        else:
            try:
                deadline = datetime.strptime(deadline, "%Y-%m-%d")
                self.tasks[task_num - 1] += f" (due {deadline.strftime('%b %d %Y')})"
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def mark_completed(self, task_num):
        if not self.tasks:
            print("No tasks added yet.")
        elif task_num > len(self.tasks) or task_num < 1:
            print("Invalid task number.")
        else:
            self.tasks[task_num - 1] += " [X]"

if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Edit a saved task")
        print("4. Delete a saved task")
        print("5. Set deadline for a task")
        print("6. Mark a task as completed")
        print("7. Exit")

        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            todo.add_task(input("\nEnter the new task: "))
        
        elif choice == "2":
            todo.view_tasks()
        
        elif choice == "3":
            num = int(input("\nEnter the number of the task you want to edit: "))
            new_task = input("\nEnter the new text for the task: ")
            todo.edit_task(num, new_task)
        
        elif choice == "4":
            num = int(input("\nEnter the number of the task you want to delete: "))
            todo.delete_task(num)
        
        elif choice == "5":
            num = int(input("\nEnter the number of the task you want to set a deadline for: "))
            deadline = input("\nEnter the deadline (YYYY-MM-DD): ")
            todo.set_deadline(num, deadline)
        
        elif choice == "6":
            num = int(input("\nEnter the number of the completed task: "))
            todo.mark_completed(num)
        
        elif choice == "7":
            break
        
        else:
            print("invalid choice , try again\n")
