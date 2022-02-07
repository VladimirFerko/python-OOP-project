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

