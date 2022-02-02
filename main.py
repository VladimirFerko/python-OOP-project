import classes
import funcs
from datetime import datetime

# main function
def main():

    # database connection
    conn = funcs.make_conn()

    # vars
    continue_var = 'Y'
    student_arr = list()
    professor_arr = list()
    courses_arr = list()

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

        vladko = classes.Student('Vladimir','Ferko', 8, 'peniazkovy')
        romanko = classes.Student('Roman','Fiut', 5, 'robkovy')
        print(vladko)
        print(romanko)

        while True:
            continue_var = input('Do you want to continue? [Y/n] ').upper()
            if continue_var == 'Y' or continue_var == 'N':
                break

    print('Goodbye')
    conn.close()
            

if __name__ == '__main__':
    main()