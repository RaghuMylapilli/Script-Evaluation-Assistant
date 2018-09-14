from tkinter import *
from contextlib import suppress
import mysql
import runtime
import spreadsheets
import setup

def get_script_output():
    roll_no = rollno_entry.get()
    path = mysql.get_script_path(roll_no)
    if path is None: return
    week_no = weekno_entry.get()
    script_name = mysql.map_script_to_week(week_no)
    if script_name is None: return
    input_text = input_entry.get()

    if runtime.execute(script_name, path, input_text) == 0:
        window.configure(background = 'white')
        file = open(path + '/op.txt', 'r')
        output = file.read()
        file.close()
    else:
        window.configure(background = 'red')
        output = 'ERROR!'

    output_var.set(output)

def increment_rollno():
    with suppress(ValueError):
        rollno_str = rollno_entry.get()
        roll_no = int(rollno_str)
        roll_no += 1
        rollno_set.set(str(roll_no))

def decrement_rollno():
    with suppress(ValueError):
        roll_no = int(rollno_entry.get())
        if roll_no == 1: return
        roll_no -= 1
        rollno_set.set(str(roll_no))

def award_grade():
    with suppress(ValueError):
        roll_no = int(rollno_entry.get())

    week_no = weekno_entry.get()
    script_name = mysql.map_script_to_week(week_no)
    if script_name is None: return
    grade = grade_entry.get()

    mysql.insert_grade(roll_no, script_name, grade)

mysql.initialise_database()

window = Tk()
window.geometry('1366x768')
window.resizable(False, False)
window.title('Shazam')

masthead = Label(window, text = 'Desiged and Developed by Shazam')
masthead.place(x = 450, y = 700, height = 50, width = 500)

output_title = Label(window, text = 'OUTPUT', relief = RAISED)
output_title.place(x = 10, y = 10, height = 30, width = 100)

output_var = StringVar()
output_label = Label(window, textvariable = output_var, relief = RAISED, anchor = NW, justify = LEFT)
output_label.place(x = 10, y = 50, height = 600, width = 550)

rollno_label = Label(window, text = 'Roll No', relief = RAISED)
rollno_label.place(x = 600, y = 50, height = 30, width = 100)

rollno_set = StringVar()
rollno_entry = Entry(window, textvariable = rollno_set)
rollno_entry.place(x = 720, y = 50, height = 30, width = 120)

weekno_label = Label(window, text = 'Week No', relief = RAISED)
weekno_label.place(x = 600, y = 100, height = 30, width = 100)

weekno_entry = Entry(window)
weekno_entry.place(x = 720, y = 100, height = 30, width = 120)

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

rollno_increment = Button(window, text = 'Next', command = increment_rollno)
rollno_increment.place(x = 870, y = 600, height = 30, width = 120)

rollno_decrement = Button(window, text = 'Previous', command = decrement_rollno)
rollno_decrement.place(x = 1020, y = 600, height = 30, width = 120)

spreadsheets_button = Button(window, text = 'SpreadSheets', command = spreadsheets.display(mysql))
spreadsheets_button.place(x = 1220, y = 50, height = 30, width = 120)

setup_button = Button(window, text = 'Setup', command = setup.display(mysql))
setup_button.place(x = 1220, y = 80, height = 30, width = 120)

window.mainloop()