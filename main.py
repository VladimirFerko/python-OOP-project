import classes
import funcs
from datetime import datetime

# main function
def main():


    continue_var = 'Y'

    # user interface for adding and showing students
    while continue_var == 'Y':
        print('''Do you want to..
    1 - add a student
    2 - add a professor
    3 - add a course
    4 - show students
    5 - show proffesors
    6 - show courses
    7 - exit''')

        while True:
            continue_var = input('Do you want to continue? [Y/n] ').upper()
            if continue_var == 'Y' or continue_var == 'N':
                break

    print('Goodbye')
            

if __name__ == '__main__':
    main()