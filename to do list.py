tasks= []
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def display_task():
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks,start=1):
            print(f"{idx}, {task}")
    else:
            print("No tasks yet!")

def delete_task():
    display_task()
    if tasks:
        try:
            idx = int(input("Enter task number to delete: "))-1
            if 0< idx <len(tasks):
              deleted_task = tasks.pop(idx)
              print(f"Deleted Task: {deleted_task}")
            else:
              print("invalid task number!")
        except ValueError:
              print("Invalid input please enter a number.")
    else:
     print("No task added yet!")

def main():
    while True:
        print("\n 1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice =='1':
            add_task()
        elif choice =='2':
            display_task()
        elif choice =='3':
            delete_task()
        elif choice =='4':
            print("Goodbye")
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()







add_task()
display_task()




