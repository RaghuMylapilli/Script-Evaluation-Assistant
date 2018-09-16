from tkinter import *
import csv
import datetime

def display(mysql):
    '''
    display()
    :return: None
    Displays the Spreadsheets UI
    '''

    def generate_spreadsheet():
        '''
        generate_spreadsheet()
        :return: None

        Generates a spreadsheet for given data
        '''
        script =  script_spinbox.get()
        grade = grade_spinbox.get()
        bound = grade_bound_spinbox.get()
        data = mysql.get_query_data(script, grade, bound)

        now = datetime.datetime.now()
        file_name = str(now.year) + '_' + str(now.month) + '_' + str(now.day)
        file_name += str(now.hour) + '_' + str(now.minute) + '_' + str(now.second)

        with open('/Users/ajayraj/Documents/Shazam/' + file_name + '.csv', 'w') as sheet:
            writer = csv.writer(sheet, delimiter = ',')
            for row in data:
                writer.writerow(row)

    window = Tk()
    window.geometry('400x300')
    window.resizable(False, False)
    window.title('Queries & SpreadSheets')

    select_label = Label(window, text = 'Get Students Data', relief = RAISED)
    select_label.place(x = 10, y = 10, height = 30, width = 300)

    script_label = Label(window, text = 'Script', relief = RAISED)
    script_label.place(x = 10, y = 50, height = 30, width = 100)

    script_spinbox = Spinbox(window, from_ = 1, to = 14)
    script_spinbox.place(x = 140, y = 50)

    grade_bound_label = Label(window, text = 'Grade Bound', relief = RAISED)
    grade_bound_label.place(x = 10, y = 90, height = 30, width = 100)

    grade_bound_spinbox = Spinbox(window, values = ('>', '=', '<'))
    grade_bound_spinbox.place(x = 140, y = 90)

    grade_label = Label(window, text = 'Grade', relief = RAISED)
    grade_label.place(x = 10, y = 140, height = 30, width = 100)

    grade_spinbox = Spinbox(window, from_ = 1, to = 15)
    grade_spinbox.place(x = 140, y = 140)

    generate_button = Button(window, text = 'Generate Spreadsheet', command = generate_spreadsheet)
    generate_button.place(x = 140, y = 180, height = 30, width = 180)

    window.mainloop()