import classes
import funcs
import sys
from datetime import datetime

# main function
def main():

    # database connection
    conn = funcs.make_conn()

    # vars
    continue_var = 'Y'
    student_arr = list()
    professor_arr = list()
    course_arr = list()

    # user interface for adding and showing students
    while continue_var == 'Y':
        print('''Do you want to..
    1 - add a student (you can add a student only if course exists)
    2 - add a professor (The professor can teach only one course)
    3 - add a course
    4 - show students
    5 - show proffesors
    6 - show courses
    7 - exit''')

        while True:
            try:
                user_choice = int(input('Which option would you like to choose? '))
                if user_choice > 0 and user_choice < 8:
                    break
            except ValueError:
                print('Int please..')

        if user_choice == 7:
            print('Goodbye')
            sys.exit(0)

        student_arr.append(classes.Student('Vladimir','Ferko', 8, 'peniazkovy'))
        student_arr.append(classes.Student('Roman','Fiut', 5, 'robkovy'))

        funcs.perform_actions(user_choice, student_arr, professor_arr, course_arr)

    conn.close()
            

if __name__ == '__main__':
    main()