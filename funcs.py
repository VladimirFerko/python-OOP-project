import psycopg2
import classes


# function makes connection with postgreSQL database
def make_conn():
    conn = psycopg2.connect(
        host = "localhost",
        database = "oop_project_data",
        user = "postgres",
        password = "password"
    )   

    return conn


def perform_actions(user_choice, student_arr, professor_arr, course_arr):
    
    # code for all possible choices
    if user_choice == 1:
        pass
    elif user_choice == 2:
        pass

    # branch for creating a course
    elif user_choice == 3:
        print('You have chosen the option number 3 - adding a course')
        cour_name = input('Insert here the name of the course: ')
        cour_spec = input('Insert here the specification of the course: ')
        course_arr.append(classes.Course(cour_name, cour_spec))

        del cour_name, cour_spec

    # branch for printing out student
    elif user_choice == 4:
        print('You have chosen the option number 4 - printing out the students')
        for student in student_arr:
            print(student)

    elif user_choice == 5:
        pass
    elif user_choice == 6:
        pass
