from tkinter import *
import csv
import datetime

def display(mysql):
    '''
    display()
    :return: None
    Displays the Spreadsheets UI
    '''

    before, after = False, False

    def set_before():
        nonlocal before, after
        before = True
        after = False

    def set_after():
        nonlocal before, after
        before = False
        after = True

    def generate_spreadsheet():
        '''
        generate_spreadsheet()
        :return: None

        Generates a spreadsheet for given data
        '''
        select = select_spinbox.get()
        date = date_entry.get()
        week = week_spinbox.get()
        grade = grade_spinbox.get()
        data = mysql.get_query_data(select, date, week, grade)

        now = datetime.datetime.now()
        file_name = select + '_' + str(now.year) + '_' + str(now.month) + '_' + str(now.day)
        file_name += str(now.hour) + '_' + str(now.minute) + '_' + str(now.second)

        with open('/Users/ajayraj/Documents/Shazam/' + file_name + '.csv', 'w') as sheet:
            writer = csv.writer(sheet, delimiter = ',')
            for row in data:
                writer.writerow(row)



    window = Tk()
    window.geometry('500x300')
    window.resizable(False, False)
    window.title('Queries & SpreadSheets')

    select_label = Label(window, text = 'Get', relief = RAISED)
    select_label.place(x = 10, y = 10, height = 30, width = 100)

    select_spinbox = Spinbox(window, values = ('Students', 'Scripts'))
    select_spinbox.place(x = 140, y = 10)

    date_label = Label(window, text = 'Date', relief = RAISED)
    date_label.place(x = 10, y = 50, height = 30, width = 100)

    before_rb = Radiobutton(window, text = 'Before', command = set_before)
    before_rb.place(x = 140, y = 50)

    after_rb = Radiobutton(window, text = 'After', command = set_after)
    after_rb.place(x = 240, y = 50)

    date_entry = Entry(window)
    date_entry.place(x = 140, y = 90, height = 30, width = 120)

    week_label = Label(window, text = 'Week', relief = RAISED)
    week_label.place(x = 10, y = 140, height = 30, width = 100)

    week_spinbox = Spinbox(window, from_ = 1, to = 14)
    week_spinbox.place(x = 140, y = 140)

    grade_label = Label(window, text = 'Grade', relief = RAISED)
    grade_label.place(x = 10, y = 180, height = 30, width = 100)

    grade_spinbox = Spinbox(window, values = ('All', 'A', 'B', 'C', 'D', 'E', 'F'))
    grade_spinbox.place(x = 140, y = 180)

    generate_button = Button(window, text = 'Generate Spreadsheet', command = generate_spreadsheet)
    generate_button.place(x = 140, y = 220, height = 30, width = 200)

    window.mainloop()