import sys
import datetime

def add_note():
    while True:
        note = input("What do you want to add: ")

        if note.strip().lower() == "!exit":
            return

        if len(note.strip()) > 0:
            break

        print('You should enter something. If you want to exit, type "!exit".')

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("notes.txt", "a") as file:
        file.write(f"{current_time} | {note}\n")

    print("The note was saved successfully!")

def view_note():
    try:
        with open("notes.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("There are no messages at this point!")
                return
            print("\nYour messages are: \n")
            for number, line in enumerate(lines, start=1):
                print(f"{number}. {line.strip()}")
    except FileNotFoundError:
        print("File couldn't be found")

def search_notes():
    try:
        search = input("What do you want to search: ")

        with open("notes.txt", "r") as file:
            wantedtext = []
            lines = file.readlines()

            for line in lines:
                if search.lower().strip() in line.lower():
                    wantedtext.append(line)

            if len(wantedtext) == 0:
                print("No matching notes found!")
                return

            for number, item in enumerate(wantedtext, start=1):
                print(f"{number}. {item.strip()}")

    except FileNotFoundError:
        print("There are no notes to search!")

def delete_note():
    try:
        with open("notes.txt", "r") as file:
            lines = file.readlines()

            if len(lines) == 0:
                print("There are no notes to delete!")
                return

    except FileNotFoundError:
        print("File does not exist!")
        return

    view_note()

    while True:
        try:
            number = int(input("Which note do you want to delete: "))

            if number > len(lines) or number <= 0:
                print("Invalid number!")
            else:
                break

        except ValueError:
            print("The value should be a number!")

    lines.pop(number - 1)

    with open("notes.txt", "w") as file:
        for line in lines:
            file.write(line)

    print("Note deleted successfully!")

def clear_notes():
    with open("notes.txt", "w") as file:
        pass

    print("All notes cleared!")

def interface():
    print("""=== NOTES MANAGER ===

1. Add Note
2. View Notes
3. Search Notes
4. Delete Note
5. Clear Notes
6. Exit: """, end="")

    while True:
        try:
            useranswer = int(input())
            break
        except ValueError:
            print("Invalid Value!")

    if useranswer == 1:
        add_note()
    elif useranswer == 2:
        view_note()
    elif useranswer == 3:
        search_notes()
    elif useranswer == 4:
        delete_note()
    elif useranswer == 5:
        clear_notes()
    elif useranswer == 6:
        sys.exit()

while True:
    interface()