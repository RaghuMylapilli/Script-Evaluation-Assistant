from tkinter import *

def display(mysql):
    '''
    display(mysql)
    :param mysql: mysql object to execute queries
    :return: None

    Displays an UI to setup students data, course plan
    '''

    def config_student():
        student_file = student_entry.get()
        mysql.init_student_table(student_file)

    def config_scripts():
        scripts_file = script_entry.get()
        mysql.init_scripts_table(scripts_file)

    '''def config_course():
        course_file = course_entry.get()'''

    window = Tk()
    window.geometry('600x100')
    window.resizable(False, False)
    window.title('Setup')

    student_label = Label(window, text = 'Student File', relief = RAISED)
    student_label.place(x = 10, y = 10, height = 30, width = 100)

    student_entry = Entry(window)
    student_entry.place(x = 140, y = 10, height = 30, width = 300)

    sconfig_button = Button(window, text = 'Configure', command = config_student)
    sconfig_button.place(x = 480, y = 10, height = 30, width = 100)

    script_label = Label(window, text = 'Scripts File', relief = RAISED)
    script_label.place(x = 10, y = 50, height = 30, width = 100)

    script_entry = Entry(window)
    script_entry.place(x = 140, y = 50, height = 30, width = 300)

    script_button = Button(window, text = 'Configure', command = config_scripts)
    script_button.place(x = 480, y = 50, height = 30, width = 100)

    '''course_label = Label(window, text = 'Course Plan', relief = RAISED)
    course_label.place(x = 10, y = 90, height = 30, width = 100)

    course_entry = Entry(window)
    course_entry.place(x = 140, y = 90, height = 30, width = 300)

    cconfig_button = Button(window, text = 'Configure', command = config_course)
    cconfig_button.place(x = 480, y = 90, height = 30, width = 100)'''

    window.mainloop()