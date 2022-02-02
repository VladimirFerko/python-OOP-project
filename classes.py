
class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def show(self):
        print(f'My name is {self.name} {self.surname}')

class Student(Person):
    def __init__(self, name, surname, grade, course):
        Person.__init__(self, name, surname)
        self.grade = grade
        self.course = course

class Professor(Person):
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course
