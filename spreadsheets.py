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
        week = week_spinbox.get()
        grade = grade_spinbox.get()
        data = mysql.get_query_data(week, grade)

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

    week_label = Label(window, text = 'Week', relief = RAISED)
    week_label.place(x = 10, y = 50, height = 30, width = 100)

    week_values = tuple(['All'] + [str(i) for i in range(1, 15)])
    week_spinbox = Spinbox(window, values = tuple(week_values))
    week_spinbox.place(x = 140, y = 50)

    grade_label = Label(window, text = 'Grade', relief = RAISED)
    grade_label.place(x = 10, y = 90, height = 30, width = 100)

    grade_spinbox = Spinbox(window, values = ('All', 'A', 'B', 'C', 'D', 'E', 'F'))
    grade_spinbox.place(x = 140, y = 90)

    generate_button = Button(window, text = 'Generate Spreadsheet', command = generate_spreadsheet)
    generate_button.place(x = 140, y = 140, height = 30, width = 180)

    window.mainloop()