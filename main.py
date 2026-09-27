from grades import grading_system, average_marks, grade_statistics
from oop import Student
import json


# Load students from JSON
with open("students.json", "r") as file:
    data = json.load(file)

students = []

for student_data in data:
    student = Student(
        student_data["ID"],
        student_data["name"],
        student_data["age"],
        student_data["course"],
        student_data["marks"],
        student_data["grade"]
    )

    students.append(student)


# Save students to JSON
def save_students():

    data = []

    for student in students:

        data.append({
            "ID": student.ID,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "grade": student.grade,
            "marks": student.marks
        })

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


def get_non_empty(prompt):

    value = input(prompt).strip()

    while value == "":
        print("This field cannot be blank.")
        value = input(prompt).strip()

    return value


def get_number(prompt):

    while True:

        value = input(prompt).strip()

        if value == "":
            print("This field cannot be blank.")
            continue

        try:
            return int(value)

        except ValueError:
            print("Please enter a valid number.")


def functionality_to_choices(options):

    if options == 1:

        ID = get_non_empty("Enter the student's ID: ")

        duplicate = False

        for student in students:

            if student.ID == ID:
                duplicate = True
                print(f"{ID} already exists.")
                break

        if not duplicate:

            name = get_non_empty("Enter the student's name: ")

            age = get_number("Enter the student's age: ")

            course = get_non_empty("Enter the student's course: ")

            new_student = Student(ID, name, age, course)

            students.append(new_student)

            print("Student added successfully!")

            save_students()


    elif options == 2:

        if not students:
            print("No students available.")
            return

        for student in students:
            student.display()


    elif options == 3:

        search = get_non_empty("Enter the student ID: ")

        found = False

        for student in students:

            if search == student.ID:

                found = True

                student.display()

                break

        if not found:
            print("Student not found. Confirm the ID entered.")


    elif options == 4:

        delete = get_non_empty("Select the ID you want to delete: ")

        deleted = False

        for student in students:

            if delete == student.ID:

                students.remove(student)

                deleted = True

                save_students()

                print("Student deleted successfully!")

                break

        if not deleted:
            print(f"{delete} does not exist.")


    elif options == 5:

        update = get_non_empty("Choose the student ID to be updated: ")

        updated = False

        for student in students:

            if update == student.ID:

                name = get_non_empty(
                    "Write the new name for the student: "
                )

                age = get_number(
                    "Write the new age for the student: "
                )

                course = get_non_empty(
                    "Write the new course for the student: "
                )

                student.update(name, age, course)

                updated = True

                save_students()

                print("Update successful!")

                break

        if not updated:
            print("The student was not found.")


    elif options == 6:

        grade = get_non_empty("Choose the student ID: ")

        graded = False

        for student in students:

            if grade == student.ID:

                while True:

                    marks = get_number(
                        "Write the student's marks: "
                    )

                    if 0 <= marks <= 100:
                        break

                    print("Marks must be between 0 and 100.")

                finalgrade = grading_system(marks)

                student.add_grade(marks, finalgrade)

                graded = True

                save_students()

                print("Grade added successfully!")

                break

        if not graded:
            print(f"{grade} was not found.")


    elif options == 7:

        result = average_marks(students)

        print(result)


    elif options == 8:

        result = grade_statistics(students)

        print(result)


def show_menu():

    return get_number(
        "\n"
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
    )


options = show_menu()

while options != 9:

    if 1 <= options <= 8:

        functionality_to_choices(options)

    else:

        print("Please choose an option between 1 and 9.")

    options = show_menu()


print("Goodbye!")