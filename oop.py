class Student:

    def __init__(self, ID, name, age, course, marks=0, grade="Not assigned"):
        self.ID = ID
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
        self.grade = grade

    def display(self):
        print(
            f"\nID: {self.ID}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Course: {self.course}\n"
            f"Grade: {self.grade}\n"
            f"Marks: {self.marks}"
        )

    def update(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def add_grade(self, marks, grade):
        self.marks = marks
        self.grade = grade