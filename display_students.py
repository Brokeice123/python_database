from main import Student


our_students = Student.select()
for student in our_students:
    print(student.name, student.age, student.id_number, student.stream, student.gender)
