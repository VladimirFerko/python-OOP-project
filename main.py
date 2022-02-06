from os import name
import classes
import funcs
import sys

# main function
def main():

    # vars
    conn = funcs.make_conn()
    school_objs = list()

    # loading objects from database
    print('Hi, please wait a moment till i load all the data')
    school_objs = funcs.load_data(conn, school_objs)
    print('Loaded succesfully')

    # case, there is no schools in the database
    if not len(school_objs):
        print('There are no schools in the database, you gotta create one..')
        name = input('What is the name of your school? ')
        adress = input('What is the adress of your school? ')
        school_objs.append(classes.School.from_user(name, adress, len(school_objs) + 1,conn))

    print(school_objs)


    conn.close()

if __name__ == '__main__':
    main()