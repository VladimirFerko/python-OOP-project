class School():
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.students = list() # list of objects
        self.professors = list() # list of objects
        self.courses = list() # list of objects

    def __str__(self):
        return f'{self.name} {self.adress}'
    
    # set methods for creating courses students and professors 

    def set_course(self, course: object):
        self.courses.append(course)

    def set_professor(self, professor: object):
        self.professors.append(professor)

    def set_student(self, student: object):
        self.students.append(student)


class Person():
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
    
class Student(Person):
    def __init__(self, name: str, surname: str, grade: int, course: str):
        Person.__init__(self, name, surname)
        self.grade = grade
        self.course = course

    def __str__(self):
        return f'Name: {self.name} \t Surname: {self.surname}\t Grade: {self.grade} \t Course: {self.course}'

class Professor(Person):
    def __init__(self, degree: str, name: str, surname: str, course: str):
        self.degree = degree
        super().__init__(name, surname)
        self.course = course

    def __str__(self):
        return f'Name: {self.degree} {self.name} \t Surname: {self.surname} \t Course: {self.course}'

class Course():
    def __init__(self, name: str, specification: str):
        self.name = name
        self.specification = specification
        self.left_space = 5
    
    def __str__(self):
        return f'Name: {self.name} \t Specification: {self.specification} \t Space left: {self.left_space}'