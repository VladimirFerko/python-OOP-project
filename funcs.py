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

def load_data():



