class Student:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.dob = ""

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_dob(self):
        return self.dob

    def student_infor(self):
        self.id = input(f"ID of student : ")
        self.name = input(f"Name of student : ")
        self.dob = input(f"Day of birth of student : ")

    def show_student(self):
        list_student = {"id": self.id, "name": self.name, "Day of Birth": self.dob}
        print(list_student)


class Courses:
    def __init__(self):
        self.cid = ""
        self.cname = ""

    def get_cid(self):
        return self.cid

    def get_cname(self):
        return self.cname

    def course_infor(self):
        self.cid = input(f"Id of course :  ")
        self.cname = input(f"Name of course :  ")

    def show_course(self):
        list_course = {"Id of course": self.cid, "Name of course": self.cname}
        print(list_course)


class Marks:
    def __init__(self):
        self.cname = ""
        self.sid = ""
        self.mark = ""

    def get_cname(self):
        return self.cname

    def get_sid(self):
        return self.sid

    def get_mark(self):
        return self.mark

    def update_marks(self):
        self.sid = input(f"Student ID: ")
        self.cname = input(f"Name of course: ")
        self.mark = int(input(f"Mark of course: "))

    def show_marks(self):
        list_mark = {'id': self.sid , 'course': self.cname, 'mark': self.mark}
        print(list_mark)


def number_students():
    count = int(input("Number of student in class : " ))
    return count


def number_course():
    course = int(input("Number of course : "))
    return course

def number_student_mark():
    student = int(input("Number of student have mark: "))
    return student

if __name__ == '__main__':
    students = []
    numberstudent = number_students()
    for i in range(0,numberstudent):
        student = Student()
        student.student_infor()
        students += [student]

    courses = []
    numbercourse = number_course()
    for i in range(0,numbercourse):
        course = Courses()
        course.course_infor()
        courses +=[course]

    marks = []
    numbermark = number_student_mark()
    for i in range(0,numbermark):
        mark = Marks()
        mark.update_marks()
        marks +=[mark]

    print("List of student:")
    for s in students:
        s.show_student()

    print("List of course:")
    for d in courses:
        d.show_course()

    print("List of marks:")
    for e in marks:
        e.show_marks()



