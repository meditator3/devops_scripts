students = []
# this gets from array and returns it
# .title() makes a lower case name to look like a title in capital
# first letter (reserved method)

def get_student_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title() #student.title() not enough
        # so we put :
        students_titlecase = student["name"].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = []
    for student in students:
        #students_titlecase = student["name"].title() # instead of repeating
        students_titlecase = get_student_titlecase() # we call the function again
    print(students_titlecase)

def add_student(name, student_id=332, ):
    student = {'name':name, 'student_id':student_id}
    students.append(student)
#def var_args(name, *args):    *args unlimited arguments not pre-defined
def var_args(name, **kwargs): # # kwargs creates the key and assigns the value proportionally.
    print(name)
    print(kwargs["description"], kwargs["feedback"]) # this prints only the value

student_list = get_student_titlecase()


student_name = input("Enter Student Name:")
student_id = input("Enter Student ID:")
add_student(student_name, student_id)
# to see how to print kwargs:
#var_args("Ariel", description="Loves Diablo IV", feedback=None)

print_students_titlecase()

