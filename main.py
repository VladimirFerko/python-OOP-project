import enum
from os import name
import classes
import funcs
import sys

# main function
def main(conn):

    # vars
    school_objs = list()

    # loading objects from database
    school_objs = funcs.load_data(conn, school_objs)

    # case, there is no schools in the database
    if not len(school_objs):
        print('There are no schools in the database, you gotta create one..')
        name, adress = funcs.get_school_vars()
        school_objs.append(classes.School.from_user(name, adress, len(school_objs) + 1,conn))

    # case, there is at least one school in the database
    else:
        print('1 - add a new school\n2 - use an existing school\n3 - exit')

        user_opt = funcs.get_user_int(1, 3)   

        # case user want to add another school 
        if user_opt == 1:
            name, adress = funcs.get_school_vars()
            school_objs.append(classes.School.from_user(name, adress, len(school_objs) + 1,conn))
            main(conn)
        
        # case user want to choose the existing school
        elif user_opt == 2:
            for index, item in enumerate(school_objs):
                print(f'{index + 1} - {item}')
            
            user_opt = funcs.get_user_int(1, len(school_objs))


            # making changes in object
            school_objs = funcs.make_changes(school_objs, user_opt, conn)

        # case user just wants to quit
        elif user_opt == 3:
            sys.exit(0)


    print(school_objs[0].courses)



if __name__ == '__main__':
    conn = funcs.make_conn()
    while True:
        main(conn)
    conn.close()
