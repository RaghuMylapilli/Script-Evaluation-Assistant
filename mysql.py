import pymysql
import csv

notes = '''
This script will tell you how to format your queries accordingly.
You have to follow this pattern.
Add necessary triggers to CreateDatabase.sql file and send a pull request.
I will further update this file with more required queries and you can fill them.
'''
database = pymysql.connect('localhost', 'root', 'anitscse034')
database.autocommit(True)
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
    db.execute("SHOW DATABASES")
    databases = db.fetchall()
    if ('SEA',) in databases:
        db.execute('USE SEA')
        return

    for file in ('CreateDatabase.sql', 'Operations.sql'):
        with open(file, 'r') as queries_file:
            queries = queries_file.read()
            query = queries.split('--')
            for i in range(0, len(query), 2):
                new_query = query[i]
                new_query = new_query.replace('\n', ' ')
                new_query = new_query.replace('\t', ' ')
                if new_query == '' or 'delimiter' in new_query.lower(): continue
                db.execute(new_query)

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
            query = "INSERT INTO Student VALUES ('%s', '%s', '%s', '%s', '%s', %s)" % tuple(student)
            db.execute(query)

def init_scripts_table(scripts_file):
    '''
    init_scripts_table(scripts_file)
    :param scripts_file: csv file containign scripts data
    :return: None

    Will insert the data from scripts_file to script table
    '''
    with open(scripts_file) as script_data:
        script_reader = csv.reader(script_data, delimiter=',')
        for script in script_reader:
            query = "INSERT INTO Script VALUES ('%s', '%s', '%s', '%s')" % tuple(script)
            db.execute(query)

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
    '''
    query = 'SELECT script_name FROM Script'
    db.execute(query)
    scripts = db.fetchall()
    script_names = (script[0] for script in scripts)
    return script_names

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

def get_input_text(script_id):
    '''
    get_input_text(script_id)
    :param script_id: The script id of the script to extract the input text
    :return: The input text
    '''
    query = "SELECT script_input FROM Script WHERE script_id = '%s'" % (script_id)
    db.execute(query)
    input_text = db.fetchall()[0][0]
    return input_text

def award_grade(reg_id, script_id, grade):
    '''
    award_grade(roll_no, script, grade)
    :param roll_no: The roll no of the student
    :param script: The script to be awarded
    :param grade: The grade to be awarded
    :return: None
    '''
    if db.execute("SELECT * FROM Grade WHERE reg_id = '%s' and script_id = '%s'" % (reg_id, script_id)) == 1:
        query = "UPDATE TABLE Grade SET grade = %s WHERE reg_id = '%s' and script_id = '%s'" % (grade, reg_id, script_id)
    else:
        query = "INSERT INTO Grade VALUES ('%s', '%s', %s)" % (reg_id, script_id, grade)
    db.execute(query)

def get_query_data(script_id, grade, bound):
    '''
    get_query_data(script_id, grade)
    :param script_id: The script id for evaluation
    :param grade: A to F
    :param bound: >, = or < the grade
    :return: query data
    '''
    if bound == 'All':
        query = "SELECT * FROM Student"
    else:
        query = "SELECT * FROM Student S, Grade G WHERE G.grade %s '%s' AND G.script_id = '%s' AND G.reg_id = S.reg_id" % (bound, grade, script_id)
    db.execute(query)
    query_data = db.fetchall()
    return query_data