import sys

tasks = []


def load_tasks():
    try:
        with open(
            r"C:\Users\renas\OneDrive\Masaüstü\Python-Projects\Day-03-File-Based-To-Do-List\tasks.txt",
            "r"
        ) as file:

            lines = file.readlines()

            for line in lines:
                row = line.strip().split(",")

                tasks.append({
                    "task": row[0],
                    "completed": row[1].strip().lower() == "true"
                })

    except FileNotFoundError:
        print("File couldn't be found!")


def save_task():
    with open(
        r"C:\Users\renas\OneDrive\Masaüstü\Python-Projects\Day-03-File-Based-To-Do-List\tasks.txt",
        "w"
    ) as file:

        for item in tasks:
            file.write(f'{item["task"]},{item["completed"]}\n')


def add_task():
    task = input("Add the task you want to complete: ")

    while True:
        if len(task.strip()):
            print("Task added successfully!")
            break
        else:
            task = input("You should enter a task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    save_task()


def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks!!")
        return

    for number, item in enumerate(tasks, start=1):
        if item["completed"]:
            print(f'{number}: [✓] {item["task"]}')
        else:
            print(f'{number}: [ ] {item["task"]}')


def complete_task():
    if len(tasks) == 0:
        print("There are no tasks!")
        return

    view_tasks()

    while True:
        try:
            tasknumber = int(
                input("Which task have you completed: ")
            )

            if tasknumber > len(tasks) or tasknumber <= 0:
                print("Enter a valid number!!")
            else:
                break

        except ValueError:
            print("You should enter a number!!")

    tasks[tasknumber - 1]["completed"] = True

    save_task()

    print("Task marked as completed!")


def delete_task():
    if len(tasks) == 0:
        print("You have no tasks!")
        return

    view_tasks()

    while True:
        try:
            tasknumber = int(
                input("Which task do you want to delete: ")
            )

            if tasknumber > len(tasks) or tasknumber <= 0:
                print("Enter a valid number!")
            else:
                break

        except ValueError:
            print("You should only enter numbers!")

    tasks.pop(tasknumber - 1)

    save_task()

    print("Task deleted successfully!")


def interface():
    print("""
=== TO-DO MANAGER ===

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
""")

    while True:
        try:
            useranswer = int(
                input("Choose: ")
            )

            if 1 <= useranswer <= 5:
                break

            print("You can enter numbers between 1-5 only!!!")

        except ValueError:
            print("You can enter numbers between 1-5 only!!!")

    if useranswer == 1:
        add_task()

    elif useranswer == 2:
        view_tasks()

    elif useranswer == 3:
        complete_task()

    elif useranswer == 4:
        delete_task()

    elif useranswer == 5:
        sys.exit()


load_tasks()

while True:
    interface()