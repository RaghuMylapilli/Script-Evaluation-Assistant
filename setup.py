import csv
from tkinter import *

def display(mysql):
    '''
    display(mysql)
    :param mysql: mysql object to execute queries
    :return: None

    Displays an UI to setup students data, course plan
    '''

    def parse_and_insert():
        student_file = student_entry.get()
        course_file = course_entry.get()

        mysql.init_student_table(student_file)
        mysql.init_course_table(course_file)

    window = Tk()
    window.geometry('500x300')
    window.resizable(False, False)
    window.title('Setup')

    student_label = Label(window, text = 'Student File', relief = RAISED)
    student_label.place(x = 10, y = 10, height = 30, width = 100)

    student_entry = Entry(window)
    student_entry.place(x = 140, y = 10, height = 30, width = 300)

    course_label = Label(window, text = 'Course Plan', relief = RAISED)
    course_label.place(x = 10, y = 50, height = 30, width = 100)

    course_entry = Entry(window)
    course_entry.place(x = 140, y = 50, height = 30, width = 300)

    submit = Button(window, text = 'Setup', command = parse_and_insert)
    submit.place(x = 140, y = 90, height = 30, width = 100)