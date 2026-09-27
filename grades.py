def grading_system(marks):

    if marks >= 80:
        return "A"

    elif marks >= 70:
        return "B-"

    elif marks >= 60:
        return "B"

    elif marks >= 50:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "Failed!"


def average_marks(students):

    if not students:
        return "No students available."

    marks = []

    for student in students:
        mark = student.marks
        marks.append(mark)

    average = sum(marks) / len(marks)

    return f"The average marks are {average:.2f}"


def grade_statistics(students):

    if not students:
        return "No students available."

    marks = []

    for student in students:
        mark = student.marks
        marks.append(mark)

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    return (
        f"Highest: {highest}\n"
        f"Lowest: {lowest}\n"
        f"Average: {average:.2f}"
    )