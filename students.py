students = []

def register_student():
    print("\n\033[32m-------Student register:-------\033[0m\n")
    students_quantity = int(input(f"\033[34mHow many students register: \034"))
    age_error = True

    for i in range(students_quantity):
        full_name = input(f"\033[1;34m {i + 1} \033[0mEnter full name: ")
        while age_error:
            try:
                age = int(input(f"\033[1;34m {i + 1} \033[0mEnter age: "))
            except ValueError:
                print("\n\033[31m-------Error: Age don't available-------\033\n[0m")
                continue
            age_error = False
        course = input(f"\033[1;34m {i + 1} \033[0mEnter course: ")
        print("")

        student_data = {
            "id_student" : len(students) + 1,
            "full_name": full_name,
            "age" : age,
            "curse": course
        }

        students.append(student_data)
    
    print("\n\033[32m-------Register succesfull.-------\033[0m")


def student_shows():

    """
    Show student to the user.

    Parameters:
        student (list) : List of the students.

    Returns:
        "Show all student to the user."
    """
    
    print("\nStudents register:")

    if len(students) == 0:
        print("List of student is empty.")
    else:
        for student in students:
            print(f"\n\033[34m ID: {student['id_student']} | Name: {student['full_name']} | Age: {student['age']} | Curse: {student['curse']}\033[0m")
            if student['curse'] != "":
                print("\n\033[32m-------Student active :)-------\033[0m")
            else:
                print("\n\033[31m-------Student inactive :(-------\033[0m")
            

def student_found():
        """
    Found the student and show to the user.

    Returns:
        "Show the student data."
    
    """
        found_student_ask = int(input("Enter a student ID: "))

        for student in students:
            if student['id_student'] == found_student_ask:
                print(f"\n\033[34m ID: {student['id_student']} | Name: {student['full_name']} | Age: {student['age']} | Curse: {student['curse']}\033[0m")
                return

        print("\n\033[31m-------Error: Student don't exist.-------\033[0m")

def student_change():
    """
    Found the student and change to data student.

    Returns:
        "Ask the change data student."
    
    """

    student_change_ask = int(input("Enter a student ID: "))

    for student in students:
        if student['id_student'] == student_change_ask:
            new_name = input("Enter a new name: ")
        
        new_age_error = True
        while new_age_error:
            try:
                new_age = int(input("Enter a new age: "))
            except ValueError:
                print("\n\033[31m-------Error: Age don't available-------\033[0m")
                continue
            new_age_error = False

            new_curse = input("Enter a new curse: ")

            if new_name != "":
                student['full_name'] = new_name
                print("\n\033[32m-------Register new name succesfull.-------\033[0m")
    
            if new_age != "":
                student['age'] = new_age
                print("\n\033[32m-------Register new age succesfull.-------\033[0m")

            if new_curse != "":
                student['curse'] = new_curse
                print("\n\033[32m-------Register new curse succesfull.-------\033[0m")

            return
            
    print("\n\033[31m-------Error: Student don't exist.-------\033[0m")

def student_delet():
    """
    Delete the student data.

    Returns:
        "Ask the ID and delate data student."
    
    """


    student_delet_ask = int(input("Enter a student ID: "))

    for student in students:
        if student['id_student'] == student_delet_ask:
            students.remove(student)
            print("\n\033[31m-------Student delete succesfull.-------\033[0m")
            return
        
    print("\n\033[31m-------Error: student ID don't exist-------\033[0m")
