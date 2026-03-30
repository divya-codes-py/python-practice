tasks = []
print("Welcome to To-Do List!")

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Quit")
    
    choice = input("Choose option: " )
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added! ✅")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif choice == "3":
        print("Goodbye! 👋")
        break
