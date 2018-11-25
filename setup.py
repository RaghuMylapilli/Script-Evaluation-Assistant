from tkinter import *
import mysql

'''
Extend the features to manage the data
'''

def display():
    '''
    display(mysql)
    :return: None

    Displays an UI to setup students data, course plan
    '''
    def open_filedialog_student():
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw()
        file_path = askopenfilename()

        nonlocal student_file, student_path
        student_file = file_path
        student_path.set(file_path)

    def open_filedialog_course():
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw()
        file_path = askopenfilename()

        nonlocal course_file, course_path
        course_file = file_path
        course_path.set(file_path)

    def open_filedialog_script():
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw()
        file_path = askopenfilename()

        nonlocal script_file, script_path
        script_file = file_path
        script_path.set(file_path)

    def config_student():
        mysql.init_student_table(student_file)

    def config_scripts():
        mysql.init_scripts_table(script_file)

    def config_course():
        mysql.init_course_outcomes(course_file)

    def config_all():
        config_student()
        config_course()
        config_scripts()

    window = Tk()
    window.geometry('600x180')
    window.resizable(False, False)
    window.title('Setup')
    window.configure(background = 'dodger blue')

    student_label = Label(window, text = 'Student File',bg='white',  relief = RAISED)
    student_label.place(x = 10, y = 10, height = 30, width = 100)

    student_path = StringVar()
    student_entry = Entry(window, textvariable = student_path)
    student_entry.place(x=140, y=10, height=30, width=300)

    student_file = ''
    student_browse_button = Button(window, text = 'Browse', bg='white', command = open_filedialog_student)
    student_browse_button.place(x = 480, y = 10, height = 30, width = 100)

    course_label = Label(window, text = "C.O's",bg='white',  relief = RAISED)
    course_label.place(x = 10, y = 50, height = 30, width = 100)

    course_path = StringVar()
    course_entry = Entry(window, textvariable = course_path)
    course_entry.place(x=140, y=50, height=30, width=300)

    course_file = ''
    course_browse_button = Button(window, text = 'Browse', bg='white', command = open_filedialog_course)
    course_browse_button.place(x = 480, y = 50, height = 30, width = 100)

    script_label = Label(window, text='Scripts File', bg='white', relief=RAISED)
    script_label.place(x=10, y=90, height=30, width=100)

    script_path = StringVar()
    script_entry = Entry(window, textvariable = script_path)
    script_entry.place(x=140, y=90, height=30, width=300)

    script_file = ''
    script_browse_button = Button(window, text = 'Browse',bg='white',  command = open_filedialog_script)
    script_browse_button.place(x=480, y=90, height=30, width=100)

    loaddata_button = Button(window, text = 'Load Data',bg='white',  command = config_all)
    loaddata_button.place(x = 480, y = 130, height = 30, width = 100)

    window.mainloop()
