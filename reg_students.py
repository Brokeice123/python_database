from main import Student
try:
    student_name = input("Enter your Name \n")
    student_age = input("Enter your Age \n")
    student_id_number = input("Enter your ID Number \n")
    student_stream = input("Enter your Stream \n")
    student_gender = input("Enter your Gender \n")

    Student.create(name=student_name, age=student_age, id_number=student_id_number, stream=student_stream,
                   gender=student_gender)
    print("Student Account Registered Successfully")


except:
    print("Registration failed. Try to use a different student ID")
