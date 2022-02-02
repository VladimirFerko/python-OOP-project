
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
    def __init__(self, name: str, surname: str, course: str):
        super().__init__(name, surname)
        self.course = course

class Course():
    def __init__(self, name: str, specification: str):
        self.name = name
        self.specification = specification
        self.left_space = 5