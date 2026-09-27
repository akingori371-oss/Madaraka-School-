from grades import grading_system,average_marks
students = [
    {
        "ID": "001",
        "name": "Anthony",
        "age": 19,
        "course": "Software Engineering",
        "grade" : "Not assigned"
    },
    {
        "ID": "002",
        "name": "Kevin",
        "age": 22,
        "course": "Data Science",
        "grade" : "Not assigned"
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
             "name": f"{Name}",
             "age": f"{age}",
             "course": f"{Course}"
         }
         students.append(new_students)
         print("Student added Successfully!") 

    elif options == 2:
        for student in students:
           print(
           f"\n ID : {student["ID"]}\n" 
           f"name: {student['name']}\n"
           f"age: {student["age"]}\n"
           f"course: {student["course"]}\n"  
           f"grade: {student['grade']}"
           )
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
        delete = input("Select the ID you want to delete")
        deleted = False
        for student in students:
           if delete == student["ID"]:
              students.remove(student)
              deleted = True

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

             student["name"] = name
             student["age"] = age
             student["course"] = course

             updated = True
             print("Update Successfull!")

        if not updated:
             print("The student was not found")  

    elif options == 6:
       grade = input("Choose the student ID")
       graded = False
       for student in students:
          if grade == student["ID"]:
           marks = int(input("Write the students marks"))
           finalgrade = grading_system(marks)
           student["marks"] = marks
           student["grade"] = f"{finalgrade}"
           graded = True
           break
       if not graded:
          print(f"{grade} was not found")
       

            

             

    else:
        print("Invalid option")


options = int(input(
    "Option 1 = Add a student\n"
    "Option 2 = View students\n"
    "Option 3 = Search Students\n"
    "Option 4 = Delete Student\n"
    "Option 5 = Update a student\n"
    "Option 6 = Add grades\n"
   
    "Choose an option: "
))


while options != :

    functionality_to_choices(options)

    options = int(input(
        "\nOption 1 = Add a student\n"
        "Option 2 = View students\n"
        "Option 3 = Search Students\n"
        "Option 4 = Delete Student\n"
        "Option 5 = Update a student\n"
        "Option 6 = add grades\n"
        "Option 7 = grade statistics"
        "Choose an option: "
    ))