students = []
# this gets from array and returns it


def get_student_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title()) #student.title() not enough

    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_student_titlecase() # we call the function again
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {'name':name, 'student_id':student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a") # this creates new file
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


student_name = input("Enter Student Name:")
student_id = input("Enter Student ID:")
add_student(student_name, int(student_id))
save_file(student_name)

read_file()
print_students_titlecase()