import pymysql

database = pymysql.connect('localhost', '', '', 'Shazam')
db = database.cursor()

def get_all(*tables):
    '''
    get_all()
    :return: list of data from all tables
    WARNING: Calling this function might result in memory leak
    '''

    all_data = []
    for table in tables:
        db.execute('SELECT * FROM ' + table)
        data = db.fetchall()
        all_data.append(data)

    return all_data

def get_script_path(roll_no):
    '''
    get_script_path(roll_no)
    :param roll_no: the roll no of the student
    :return: the path of his scripts
    '''
    pass

def map_script_to_week(week_no):
    '''
    map_scipt_to_week(week_no)
    :param week_no: the week number to do a particular program
    :return: the script/program to be done in that week
    '''
    pass

def insert_grade(roll_no, script, grade):
    '''
    insert_grade(roll_no, script)
    :param roll_no: The roll no of the student
    :param script: The script to be awarded
    :param grade: The grade to be awarded
    :return: None
    '''
    pass

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
