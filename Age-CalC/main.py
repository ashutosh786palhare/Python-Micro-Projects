from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

def clear_all():
    date_picker.delete(0, END)
    given_date_picker.delete(0, END)
    rslt_year_field.delete(0, END)
    rslt_month_field.delete(0, END)
    rslt_day_field.delete(0, END)

def calculate_age():
    birth_date = date_picker.get_date()
    given_date = given_date_picker.get_date()

    if not birth_date or not given_date:
        messagebox.showerror("Input Error", "Please select both birth date and given date.")
        return

    birth_year, birth_month, birth_day = birth_date.year, birth_date.month, birth_date.day
    given_year, given_month, given_day = given_date.year, given_date.month, given_date.day
    
    # Age calculation logic
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if birth_day > given_day:
        given_month -= 1
        given_day += month[birth_month - 1]

    if birth_month > given_month:
        given_year -= 1
        given_month += 12

    calculated_day = given_day - birth_day
    calculated_month = given_month - birth_month
    calculated_year = given_year - birth_year
    
    # Display the calculated age in a popup message
    result_message = f"Calculated Age:\nYears: {calculated_year}\nMonths: {calculated_month}\nDays: {calculated_day}"
    messagebox.showinfo("Age Calculation Result", result_message)

root = Tk()
root.title('Age Calculator by AP')
root.geometry('600x400')
root.configure(bg='light grey')

date_picker = DateEntry(root, width=12, background='blue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
date_picker.grid(row=1, column=1, padx=10, pady=10)

given_date_picker = DateEntry(root, width=12, background='blue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
given_date_picker.grid(row=1, column=4, padx=10, pady=10)

resultant_age = Button(root, text="Resultant Age", font=('Arial', 12, 'bold'), bd=5, relief=RAISED, bg='light blue', fg='black', command=calculate_age)
resultant_age.grid(row=4, column=2)

clear_all_entry = Button(root, text="Clear All Output", font=('Arial', 12, 'bold'), bd=5, relief=RAISED, bg='light blue', fg='black', command=clear_all)
clear_all_entry.grid(row=12, column=2)

root.mainloop()
