from cgi import test
from tempfile import tempdir
import classes
import os
import psycopg2

# make connection wit postgres

def make_conn():
    conn = psycopg2.connect(
        host = "localhost",
        database = "oop_project_data",
        user = "postgres",
        password = "password"
    )   

    return conn


# loading data from postgres

def load_data(conn, school_objs):

    # loading school objects 

    with conn.cursor() as cur:
        cur.execute('''
        SELECT school_name, school_adress 
        FROM "Schools"
        ''')
        temp = cur.fetchall()

        for item in temp:
            school_objs.append(classes.School(item[0], item[1]))

    # loading course objects
    
        for index in range(len(school_objs)):  
            cur.execute(f'''
            SELECT course_name, course_specification, left_space
            FROM "Courses"
            WHERE school_id = {index + 1}
            '''
            )
            temp = cur.fetchall()

            for item in temp:
                school_objs[index].set_course(classes.Course(item[0], item[1], item[2]))


            # loading professor objects

            cur.execute(f'''
            SELECT professor_degree, professor_name, professor_surname, course_name
            FROM "Professors"
            INNER JOIN "Courses"
            ON "Professors".id_course = "Courses".id_course
            WHERE "Professors".school_id = {index + 1}
            '''
            )
            temp = cur.fetchall()

            for item in temp:
               school_objs[index].set_professor(classes.Professor(item[0], item[1], item[2], item[3]))

            # loading student objects
            cur.execute(f'''
            SELECT student_name, student_surname, student_grade, course_name
            FROM "Students"
            INNER JOIN "Courses"
            ON "Students".id_course = "Courses".id_course
            WHERE "Students".school_id = {index + 1}
            '''
            )
            temp = cur.fetchall()

            for item in temp:
                school_objs[index].set_student(classes.Student(item[0], item[1], item[2], item[3]))

            temp = list()

    return school_objs 

# func for getting school info

def get_school_vars():
    name = input('What is the name of your school? ')
    adress = input('What is the adress of your school? ')

    return name, adress

# func for getting int user input

def get_user_int(low, top):

    while True:
        try:
            user_opt = int(input('Which option would you like to choose? '))
            if user_opt >= low and user_opt <= top:
                break
        except ValueError:
            print('Int please..')

    return user_opt

# func for operating with school object

def make_changes(school_objs, user_opt, conn):
    continue_var = 'Y'

    while continue_var == 'Y':
        print(f'Now You can modify the: {school_objs[user_opt - 1]}')    
        print('''1 - add course
2 - add professor
3 - add student   
4 - show courses
5 - show professors
6 - show students     
        ''')

        feature_opt = get_user_int(1, 6)

        # case user selected adding a course
        if feature_opt == 1: 
            school_objs[user_opt - 1].set_course(classes.Course.from_user(conn, user_opt))

        # case user selected adding a professor 
        if feature_opt == 2: 

            if not len(school_objs[user_opt - 1].courses):
                print('First you need to create a course to hire a professor')

            else:

                # getting taken courses
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(f'''SELECT course_name from "Professors" 
                        INNER JOIN "Courses" ON "Professors".id_course = "Courses".id_course 
                        WHERE "Professors".school_id = {user_opt}''')
                        taken_courses = cur.fetchall()

                # getting free courses

                free_courses = list()

                for item in school_objs[user_opt - 1].courses:
                    free_courses.append(item.name)

                for item in taken_courses:
                    for course in free_courses:
                        if item[0] == course:
                            free_courses.remove(item[0])

                # creating professor feature   

                if len(free_courses):
                    print('There are all free courses')
                    for index, course in enumerate(free_courses):
                        print(f'{index + 1} - {course}')

                    professor_course = get_user_int(1, len(free_courses))

                    school_objs[user_opt - 1].set_professor(classes.Professor.from_user(conn, free_courses[professor_course - 1], len(school_objs[user_opt - 1].professors), user_opt))

                # just in case, user dont have any course without professor
                else:
                    print('You dont have any free course for your professor')
                        

            
        # case user selected adding a student 
        if feature_opt == 3:

            # getting free course informations
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f'''
                    SELECT id_course, course_name, school_id
                    FROM "Courses"
                    WHERE school_id = {user_opt} AND left_space > 0
                    ORDER BY id_course ASC
                    ''')

                    cours = cur.fetchall()

                    # getting student info
                    student_name = input('Whats the name of the student? ')
                    student_surname = input('Whats the surname of the student? ')

                    while True:
                        try:
                            student_grade = int(input('Whats the grade of the student? [1 - 5] '))
                            if student_grade > 0 and student_grade < 6:
                                break
                        except ValueError:
                            print('Int please..') 

                    # asking for selecting 
                    indexes = list()
                    for index in range(len(cours)):
                        print(f'{cours[index][0]} - {cours[index][1]}')
                        indexes.append(cours[index][0])
                    
                    while True:
                        try:
                            student_cour = int(input('Which course would you like to choose? '))
                            if student_cour in indexes:
                                break
                        except ValueError:
                            print('Int please..')
                        
                    for item in cours:
                        if item[0] == student_cour:
                            student_course = item[1]
                            break

                    cur.execute(f'''
                    INSERT INTO "Students" (student_id ,student_name, student_surname, student_grade, id_course, school_id)
                    VALUES ({len(school_objs[user_opt - 1].students) + 1}, '{student_name}', '{student_surname}', {student_grade}, {student_cour}, {user_opt})                    
                    '''
                    )

                    cur.execute(f'''
                    UPDATE "Courses"
                    SET left_space = left_space - 1
                    WHERE id_course = {student_cour}
                    ''')

            school_objs[user_opt - 1].students.append(classes.Student.from_user(student_name, student_surname, student_grade, student_course))

            
            for index, item in enumerate(school_objs[user_opt - 1].courses):
                if item.name == student_course:
                    idx = index
                    break

            school_objs[user_opt - 1].courses[idx].set_space()

        # case user selected showing courses
        if feature_opt == 4:
            print('You have selected - show courses')
            print(f'School - {school_objs[user_opt - 1]}')

            if len(school_objs[user_opt - 1].courses):
                for item in school_objs[user_opt - 1].courses:
                    print(item)

            else:
                print('There are no courses')

        # case user selected showing professors
        if feature_opt == 5:
            print('You have selected - show professors')
            print(f'School - {school_objs[user_opt - 1]}')

            if len(school_objs[user_opt - 1].professors):
                for item in school_objs[user_opt - 1].professors:
                    print(item)

            else:
                print('There are no professors')

        # case user selected showing students
        if feature_opt == 6:
            print('You have selected - show students')
            print(f'School - {school_objs[user_opt - 1]}')

            if len(school_objs[user_opt - 1].students):
                for item in school_objs[user_opt - 1].students:
                    print(item)

            else:
                print('There are no students')


        while True:
            continue_var = input('Do you want to continue? [Y/n] ').upper()
            if continue_var == 'Y':
                make_changes(school_objs, user_opt, conn)
            elif continue_var == 'N':
                return school_objs

