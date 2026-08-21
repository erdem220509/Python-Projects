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
        print("Enter 1,2,3 or 4!!!")

def add_student():
    grades = []
    name = input("Please enter students name: ").strip()
    while True:
        try:
            grade = float(input("Please enter grades one by one (Type done in case you want to quit): "))
            grades.append(grade)

            if not (grade>=0 and grade<=100):
                raise ValidationError("The note should be between 1 and 100!!! ")

            if grade.lower().strip() == "done":
                print(f"{name} has added succesfully!!")
                break
        except ValueError:
            print("Grade should be a value between 1 and 100!!!")
        except ValidationError:
            print("Grade should be a value between 1 and 100!!!")
        

    totalgrade = 0
    lettergrade = ""

    for grade in grades:
        totalgrade += grade
    if len(grades) > 0:
        average = totalgrade/len(grades)
    else:
        print("You should enter at least 1 grade!!")

    if average >90 and average <100:
        lettergrade = "A"
    elif average >80 and average <= 90:
        lettergrade = "B"
    elif average > 70 and average <= 80:
        lettergrade = "C"
    elif average > 60 and average <= 70:
        lettergrade = "D"
    elif average <= 60:
        lettergrade = "F"
    else:
        print("Ivalid scores")

    students.append({
        "name": name,
        "grades": grades,
        "average": average,
        "lettergrade": lettergrade
    })

def view_student():
    for student in students:
        print(f"{student["name"]}")
        print("Grades: ", end="")
        for item in student.get("grades"):
            print(item, end=" ")
        print(f"Average: {student["average"]}")
        print(f"Letter grade: {student["lettergrade"]}")

def view_top_student():
    highest_note = None
    highest_note_person = None
    for student in students:
        if highest_note == None or student["average"] > highest_note:
            highest_note_person = student["name"]
    print(f"Top student is {highest_note_person}")
    print(f"Average: {highest_note}")


while True:
    interface()