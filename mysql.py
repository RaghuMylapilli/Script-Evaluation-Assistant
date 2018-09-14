import pymysql
import csv

notes = '''
This script will tell you how to format your queries accordingly.
You have to follow this pattern.
Add necessary triggers to CreateDatabase.sql file and send a pull request.
I will further update this file with more required queries and you can fill them.
'''
database = pymysql.connect('localhost', 'root', 'anitscse034')
db = database.cursor()

def initialise_database():
    '''
    initialse_database()
    :return: None
    creates database
    creates tables
    adds constraints
    creates triggers and funcs
    '''
    db.execute("SHOW DATABASES LIKE 'Shazam'")
    databases = db.fetchall()
    if ('Shazam',) in databases:
        db.execute('USE Shazam')
        return

    with open('CreateDatabase.sql', 'r') as queries_file:
        queries = queries_file.read()
        query = queries.split('--')
        for i in range(0, len(query), 2):
            query[i].replace('\n', '')
            if query[i] == '': continue
            db.execute(query[i])

def get_script_path(roll_no):
    '''
    get_script_path(roll_no)
    :param roll_no: the roll no of the student
    :return: the path of his scripts
    '''
    query = 'SELECT dir FROM Student where regid = %s' % (roll_no)
    db.execute(query)
    data = db.fetchall()

def map_script_to_week(week_no):
    '''
    map_scipt_to_week(week_no)
    :param week_no: the week number to do a particular program
    :return: the script/program to be done in that week
    '''
    query = 'SELECT script FROM CoursePlan WHERE week = %s' % (week_no)
    db.execute(query)
    data = db.fetchall()
    scripts = [script[0] for script in data]
    return scripts

def insert_grade(roll_no, script, grade):
    '''
    insert_grade(roll_no, script)
    :param roll_no: The roll no of the student
    :param script: The script to be awarded
    :param grade: The grade to be awarded
    :return: None
    '''
    query = 'UPDATE TABLE PythonScript SET grade = %s WHERE regid = %s and script = %s' % (grade, roll_no, script)
    db.execute(query)


def get_query_data(select, date, week, grade, before, after):
    '''
    get_query_data(select, date, week, grade, before, after
    :param select: What to select
    :param date: When to select
    :param week: Which week
    :param grade: A to F
    :param before: True if yes
    :param after: True if yes
    :return: query data
    '''
    pass

def init_student_table(student_file):
    '''
    init_student_table(student_file):
    :param student_file: csv file containing students data
    :return: None

    Will insert the data from student_file to student table
    '''
    with open(student_file) as student_data:
        student_reader = csv.reader(student_data, delimiter = ',')
        for student in student_reader:
            query = "INSERT INTO Student VALUES ('%s', '%s', '%s', '%s', '%s', %s, '%s')" % tuple(student)
            db.execute(query)


def init_course_table(course_file):
    '''
    init_course_table(course_file)
    :param course_file: csv file containg week to script mapping
    :return: None

    Will insert the data from course_file to course plan table
    '''
    with open(course_file) as course_data:
        course_reader = csv.reader(course_data, delimiter = ',')
        for course_map in course_reader:
            query = "INSERT INTO CoursePlan VALUES (%s, '%s')" % tuple(course_map)
            db.execute(query)