from grades import grading_system, average_marks, grade_statistics
from oop import Student
import json

with open("students.json", "r") as file:
    students = json.load(file)


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def functionality_to_choices(options):

    if options == 1:
        id = input("Enter the students ID")
        duplicate = False

        for student in students:
            if student["ID"] == id:
                duplicate = True
                print(f"{id} already exists")
                break

        if not duplicate:
            Name = input("Enter the students name")
            age = input("Enter the students age")
            Course = input("Enter the students Course")

            new_student = Student(id, Name, age, Course)

            students.append(new_student)
          
            print("Student added Successfully!")
            save_students()

    elif options == 2:
        for student in students:
          new_student = Student(id, Name, age, Course)
          students.append(new_student)

    elif options == 3:
        search = input("Enter the student ID")
        found = False

        for student in students:
            if search == student["ID"]:
                found = True
                print(
                    f"{student['name']}\n"
                    f"{student['age']}\n"
                    f"{student['course']}\n"
                )
                break

        if not found:
            print("Student not found confirm the ID entered")

    elif options == 4:
        delete = input("Select the ID you want to delete")
        deleted = False

        for student in students:
            if delete == student["ID"]:
                students.remove(student)
                deleted = True
                save_students()
                print("Student deleted successfully!")
                break

        if not deleted:
            print(f"{delete} does not exist")

    elif options == 5:
        update = input("Choose the student ID to be updated")
        updated = False

        for student in students:
            if update == student["ID"]:
                name = input("Write the new name for the student")
                age = input("Write the new age for the student")
                course = input("Write the new course for the student")

                student.update(name, age, course)

                updated = True
                save_students()
                print("Update Successfull!")
                break

        if not updated:
            print("The student was not found")

    elif options == 6:
        grade = input("Choose the student ID")
        graded = False

        for student in students:
            if grade == student["ID"]:
                marks = int(input("Write the students marks"))
                finalgrade = grading_system(marks)

                student.add_grade(marks, finalgrade)

                graded = True
                save_students()
                print("Grade added successfully!")
                break

        if not graded:
            print(f"{grade} was not found")

    elif options == 7:
        result = average_marks(students)
        print(result)

    elif options == 8:
        result = grade_statistics(students)
        print(result)


options = int(input(
    "Option 1 = Add a student\n"
    "Option 2 = View students\n"
    "Option 3 = Search Students\n"
    "Option 4 = Delete Student\n"
    "Option 5 = Update a student\n"
    "Option 6 = Add grades\n"
    "Option 7 = Average marks\n"
    "Option 8 = Statistics\n"
    "Option 9 = Exit\n"
    "Choose an option: "
))

while options != 9:

    functionality_to_choices(options)

    options = int(input(
        "\nOption 1 = Add a student\n"
        "Option 2 = View students\n"
        "Option 3 = Search Students\n"
        "Option 4 = Delete Student\n"
        "Option 5 = Update a student\n"
        "Option 6 = Add grades\n"
        "Option 7 = Average marks\n"
        "Option 8 = Statistics\n"
        "Option 9 = Exit\n"
        "Choose an option: "
    ))