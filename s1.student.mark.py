# Students
def number_students():
    count = int(input("Number of student in class : " ))
    return count

def student_infor():
        id = input("ID of student : ")
        name = input("Name of student : ")
        birthday = input("Day of birth of student : ")
        list_student = {"id":id , "name":name , "Day of Birth":birthday}
        return list_student

def list_student():
    students = []
    number = number_students()
    for i in range(0, number):
        list_student = student_infor()
        students += [list_student]
    print("List of student : ")
    print(students)



# Courses
def number_course():
    course = int(input("Number of course : "))
    return course

def course_infor():
        course_id = input("Id of course : ")
        course_name = input("Name of course : ")
        list_course = {"Id of course":course_id , "Name of course":course_name}
        return list_course

def list_course():
    courses = []
    number_courses = number_course()
    for i in range(1, number_courses):
        list_course = course_infor()
        courses += [list_course]
    print("List of course : ")
    print(courses)



# mark
def number_mark():
    student = int(input("Number of mark we have for student: "))
    return student


def update_marks():
    student_id = input("Student ID: ")
    course = input("Name of course: ")
    mark = int(input("Mark of course: "))
    list_mark = {'id':student_id , 'course':course , 'mark':mark}
    return list_mark

def list_mark():
    mark = []
    mark = number_mark()
    for i in range(0, mark):
        list_mark = update_marks()
        mark += [list_mark]
    print(mark)

number_students()
list_student()

number_course()
list_course()

number_mark()
list_mark()