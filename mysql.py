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

    for file in ('CreateDatabase.sql', 'Operations.sql'):
        with open(file, 'r') as queries_file:
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
    query = 'SELECT dir FROM Student where reg_id = %s' % (roll_no)
    db.execute(query)
    data = db.fetchall()
    directory = data[0][0]
    return directory

def get_script_names():
    '''
    get_script_names()
    :return: returns a tuple of all script names

    query = 'SELECT script_name FROM Script'
    db.execute(query)
    scripts = db.fetchall()
    script_names = (script[0] for script in scripts)
    return script_names
    '''
    script_names = ['script ' + str(i) for i in range(1, 11)]
    return tuple(script_names)

def get_script(script_id):
    '''
    get_script(reg_id,, script_id)
    :param reg_id: Registration id of student
    :param script_id: Script id
    :return: The script_name
    '''
    query = "SELECT script_name FROM Script WHERE script_id = '%s'" % (script_id)
    db.execute(query)
    script = db.fetchall()
    return script[0][0]

def insert_grade(roll_no, script, grade):
    '''
    insert_grade(roll_no, script, grade)
    :param roll_no: The roll no of the student
    :param script: The script to be awarded
    :param grade: The grade to be awarded
    :return: None
    '''
    query = "UPDATE TABLE Grade SET grade = %s WHERE reg_id = '%s' and script_id = '%s'" % (grade, roll_no, script)
    db.execute(query)


def get_query_data(week, grade):
    '''
    get_query_data(week, grade)
    :param week: Which week
    :param grade: A to F
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