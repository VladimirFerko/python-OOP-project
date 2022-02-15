import psycopg2

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

    @classmethod
    def from_user(cls, name, adress, idx, conn):
        with conn:
            with conn.cursor() as cur:
                cur.execute(f'''
                    INSERT INTO "Schools" (school_id, school_name, school_adress)
                    VALUES ({idx}, N'{name}', N'{adress}');
                '''
                )

        return cls(name, adress)


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

    @classmethod
    def from_user(cls, name, surname, grade, course):
        return cls(name, surname, grade, course)




class Professor(Person):
    def __init__(self, degree: str, name: str, surname: str, course: str):
        self.degree = degree
        super().__init__(name, surname)
        self.course = course

    def __str__(self):
        return f'Name: {self.degree} {self.name} \t Surname: {self.surname} \t Course: {self.course}'

    @classmethod
    def from_user(cls, conn, course, prof_idx, user_opt):
        while True:
            # asking if the professor has degree
            qt_degree = input('Does this teacher have a degree? [Y/n] ').upper()
            if qt_degree == 'Y' or qt_degree == 'N':
                break
        
        # asking for professor informations
        if qt_degree == 'Y':
            while True:
                degree_var = input('Insert professors degree here: ')
                if len(degree_var) < 6:
                    break

            name = input('Insert professors name here: ')
            surname = input('Insert professors surname here: ')

            # getting id of the certain course
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f'''
                    SELECT id_course
                    FROM "Courses"
                    WHERE course_name = '{course}'
                    ''')

                    id_course = cur.fetchone()
            
                    # writing data into postgres

                    cur.execute(f'''
                    INSERT INTO "Professors" (id_professor, professor_degree, professor_name, professor_surname, id_course, school_id)
                    VALUES ({prof_idx + 1}, '{degree_var}', '{name}', '{surname}',{id_course[0]}, {user_opt});
                    ''')


        else:
            # professor info
            name = input('Insert professors name here: ')
            surname = input('Insert professors surname here: ')

            # getting id of the certain course
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f'''
                    SELECT id_course
                    FROM "Courses"
                    WHERE course_name = '{course}'
                    ''')

                    id_course = cur.fetchone()
            
                    # writing data into postgres

                    cur.execute(f'''
                    INSERT INTO "Professors" (id_professor, professor_degree, professor_name, professor_surname, id_course, school_id)
                    VALUES ({prof_idx + 1}, NULL, '{name}', '{surname}',{id_course[0]}, {user_opt});
                    ''')

class Course():
    def __init__(self, name: str, specification: str):
        self.name = name
        self.specification = specification
        self.left_space = 5
    
    def __str__(self):
        return f'Name: {self.name} \t\t\t Specification: {self.specification} \t\t\t Space left: {self.left_space}'

    @classmethod
    def from_user(cls, conn, user_opt):
        # input vars
        name = input('Whats the name of the course? ')
        specification = input('What is the specification of this couse? ')

        # writing into postgres
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    f'SELECT id_course from "Courses" WHERE school_id = {user_opt}'
                )
                idx = cur.fetchall()

                if not len(idx):
                    cur.execute(f'''
                INSERT INTO "Courses" (id_course, course_name, course_specification, school_id, left_space)
                VALUES (1, '{name}', '{specification}', '{user_opt}', 5); 
            ''')
                else:

                    cur.execute(f'''
                INSERT INTO "Courses" (id_course, course_name, course_specification, school_id, left_space)
                VALUES ({idx[-1][0] + 1}, '{name}', '{specification}', {user_opt}, 5); 
            ''')

        return cls(name, specification)
