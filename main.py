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

    print(len(school_objs))

if __name__ == '__main__':
    main()