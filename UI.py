from tkinter import *
import mysql
import runtime
import spreadsheets
import setup

def get_script_output():
    roll_no = regid_var.get()
    path = mysql.get_script_path(roll_no)
    #week_no = weekno_optionmenu.get()
    script_name = script_var.get()
    script_id = mysql.get_script_id(script_name)
    input_text = input_entry.get()
    if input_text == '***':
        input_text = mysql.get_input_text(script_id)
    language = mysql.get_script_runtime(script_id)

    if runtime.execute(script_name, language, path, input_text) == 0:
        file = open(path + '/op.txt', 'r')
        output = file.read()
        file.close()
        window.configure(background='light blue')
    else:
        window.configure(background = 'red')
        output = 'ERROR!'

    output_var.set(output)

def award_grade():
    try:
        roll_no = int(regid_var.get())
    except:
        return

    script_name = script_var.get()
    script_id = mysql.get_script_id(script_name)
    grade = grade_entry.get()
    mysql.award_grade(roll_no, script_id, grade)

def display_spreadsheets_ui():
    spreadsheets.display()

def display_setup_ui():
    setup.display()

def weekno_command(week_no):
    global script_names, script_var, scriptname_optionmenu
    script_names = mysql.get_script_names_for_week(week_no)
    script_var.set(script_names[0])
    scriptname_optionmenu = OptionMenu(window, script_var, *script_names, command=scriptname_command)
    scriptname_optionmenu.place(x=800, y=100, height=30, width=200)


def scriptname_command():
    pass

mysql.initialise_database()

window = Tk()
window.geometry('1440x900')
window.resizable(False, False)
window.title('Script Evaluation Assistant')
window.configure(background = 'light blue')

masthead = Label(window, text = 'Desiged and Developed by Shazam')
masthead.place(x = 450, y = 700, height = 50, width = 500)

output_title = Label(window, text = 'OUTPUT', relief = RAISED)
output_title.place(x = 10, y = 10, height = 30, width = 100)

output_var = StringVar()
output_label = Label(window, textvariable = output_var, relief = RAISED, anchor = NW, justify = LEFT)
output_label.place(x = 10, y = 50, height = 600, width = 550)

rollno_label = Label(window, text = 'Roll No', relief = RAISED)
rollno_label.place(x = 600, y = 50, height = 30, width = 100)

reg_ids = mysql.get_student_regids()
regid_var = StringVar(window)
regid_var.set(reg_ids[0])
rollno_optionsmenu = OptionMenu(window, regid_var, *reg_ids)
rollno_optionsmenu.place(x = 720, y = 50, height = 30, width = 150)

script_spec = Label(window, text = 'Week & Script', relief = RAISED)
script_spec.place(x = 600, y = 100, height = 30, width = 100)

weeks = mysql.get_weeks_list()
week_var = StringVar(window)
week_var.set(weeks[0])
week_no = OptionMenu(window, week_var, *weeks, command = weekno_command)
week_no.place(x = 720, y = 100, height = 30, width = 70)

script_names = mysql.get_script_names_for_week('1')
script_var = StringVar(window)
script_var.set(script_names[0])
scriptname_optionmenu = OptionMenu(window, script_var, *script_names, command = scriptname_command)
scriptname_optionmenu.place(x = 800, y = 100, height = 30, width = 200)

input_label = Label(window, text = 'Input', relief = RAISED)
input_label.place(x = 600, y = 150, height = 30, width = 100)

input_entry = Entry(window)
input_entry.place(x = 720, y = 150, height = 300, width = 500)

getop_button = Button(window, text = 'Get Output', command = get_script_output)
getop_button.place(x = 720, y = 480, height = 30, width = 140)

grade_label = Label(window, text = 'Grade', relief = RAISED)
grade_label.place(x = 600, y = 550, height = 30, width = 100)

grade_entry = Entry(window)
grade_entry.place(x = 720, y = 550, height = 30, width = 120)

grade_button = Button(window, text = 'Award Grade', command = award_grade)
grade_button.place(x = 720, y = 600, height = 30, width = 120)

spreadsheets_button = Button(window, text = 'SpreadSheets', command = display_spreadsheets_ui)
spreadsheets_button.place(x = 1220, y = 50, height = 30, width = 120)

setup_button = Button(window, text = 'Setup', command = display_setup_ui)
setup_button.place(x = 1220, y = 80, height = 30, width = 120)

window.mainloop()