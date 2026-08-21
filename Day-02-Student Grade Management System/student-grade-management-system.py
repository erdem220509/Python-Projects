import sys

students = []


def interface():
    print("""=== STUDENT GRADE MANAGER ===

    1. Add student
    2. View students
    3. Show top student
    4. Exit""")

    while True:
        try:
            useranswer = int(input("Choose what you want to do in numbers only: "))
            break
        except ValueError:
            print("You should enter numbers!!")

    if useranswer == 1:
        add_student()

    elif useranswer == 2:
        view_student()

    elif useranswer == 3:
        view_top_student()

    elif useranswer == 4:
        sys.exit()

    else:
        print("Enter 1, 2, 3 or 4!!!")


def add_student():
    grades = []

    name = input("Please enter student's name: ").strip()

    while True:
        try:
            grade_input = input(
                "Please enter grades one by one "
                "(Type done in case you want to quit): "
            )

            if grade_input.lower().strip() == "done":

                if len(grades) == 0:
                    print("You should enter at least 1 grade!!")
                    continue

                print(f"{name} has been added successfully!!")
                break

            grade = float(grade_input)

            if not (0 <= grade <= 100):
                raise ValueError

            grades.append(grade)

        except ValueError:
            print("Grade should be a value between 0 and 100!!!")

    totalgrade = 0

    for grade in grades:
        totalgrade += grade

    average = totalgrade / len(grades)

    if average >= 90:
        lettergrade = "A"

    elif average >= 80:
        lettergrade = "B"

    elif average >= 70:
        lettergrade = "C"

    elif average >= 60:
        lettergrade = "D"

    else:
        lettergrade = "F"

    students.append({
        "name": name,
        "grades": grades,
        "average": average,
        "lettergrade": lettergrade
    })


def view_student():

    if len(students) == 0:
        print("There are no students yet!")
        return

    for student in students:

        print(f"\n{student['name']}")

        print("Grades: ", end="")

        for item in student["grades"]:
            print(item, end=" ")

        print()

        print(f"Average: {student['average']:.2f}")
        print(f"Letter grade: {student['lettergrade']}")


def view_top_student():

    if len(students) == 0:
        print("There are no students yet!")
        return

    highest_note = None
    highest_note_person = None

    for student in students:

        if highest_note is None or student["average"] > highest_note:
            highest_note = student["average"]
            highest_note_person = student["name"]

    print(f"Top student is {highest_note_person}")
    print(f"Average: {highest_note:.2f}")


while True:
    interface()