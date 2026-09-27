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

    marks = []

    for student in students:
        mark = student["marks"]
        marks.append(mark)

    average = sum(marks) / len(students)

    return f"The average marks are {average}"