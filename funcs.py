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
                school_objs[index].set_course(classes.Course(item[0], item[1]))


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

            print('There are all free courses left')
            for index, course in enumerate(free_courses):
                print(f'{index + 1} - {course}')
            professor_course = get_user_int(1, len(free_courses))


                        

            
        # case user selected adding a student 
        if feature_opt == 3:
            pass

        # case user selected showing courses
        if feature_opt == 4:
            print('You have selected - show courses')
            print(f'School - {school_objs[user_opt - 1]}')

            if len(school_objs[user_opt - 1]. courses):
                for item in school_objs[user_opt - 1].courses:
                    print(item)

            else:
                print('There are no courses')

        # case user selected showing professors
        if feature_opt == 5:
            pass

        # case user selected showing students
        if feature_opt == 6:
            pass


        while True:
            continue_var = input('Do you want to continue? [Y/n] ').upper()
            if continue_var == 'Y' or continue_var == 'N':
                break

        return school_objs

