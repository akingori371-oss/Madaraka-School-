students = [
    {
        "ID": "001",
        "name": "Anthony",
        "age": 19,
        "course": "Software Engineering"
    },
    {
        "ID": "002",
        "name": "Kevin",
        "age": 22,
        "course": "Data Science"
    }
]


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

         new_students = {
         
             "ID": f"{id}",
             "Name": f"{Name}",
             "Age": f"{age}",
             "Course": f"{Course}"
         }
         students.append(new_students)
         print("Student added Successfully!") 

    elif options == 2:
        for student in students:
           print(
           f"\n ID : {student["ID"]}\n" 
           f"name: {student["name"]}\n"
           f"age: {student["age"]}\n"
           f"course: {student["course"]}"  )

    elif options == 3:
      search = input("Enter the student ID")
      found = False
      for student in students:
         if search == student["ID"]:
            found = True
            print(
               f"{student["name"]}\n"
               f"{student["age"]}\n"
               f"{student["course"]}\n"
            )
            break
         
         if not found:
            print("Student not found confirm the ID entered")  
    elif options == 4:
        print("Delete Student Selected")
    elif options == 5:
        print("Exiting...")
    else:
        print("Invalid option")


options = int(input(
    "Option 1 = Add a student\n"
    "Option 2 = View students\n"
    "Option 3 = Search Students\n"
    "Option 4 = Delete Student\n"
    "Option 5 = Exit\n"
    "Choose an option: "
))


while options != 5:

    functionality_to_choices(options)

    options = int(input(
        "\nOption 1 = Add a student\n"
        "Option 2 = View students\n"
        "Option 3 = Search Students\n"
        "Option 4 = Delete Student\n"
        "Option 5 = Exit\n"
        "Choose an option: "
    ))