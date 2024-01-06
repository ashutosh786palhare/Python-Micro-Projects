import tkinter as tk
from tkinter import messagebox
import requests
import webbrowser

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Currency Converter by AP')
        self.master.geometry('470x550')  
        self.master.configure(bg='#ffcc00')  
        self.currency_list = {}  

        self.menu_bar = tk.Menu(master)
        self.master.config(menu=self.menu_bar)

        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label='About', command=self.show_about)
        self.menu_bar.add_cascade(label='About', menu=self.about_menu)

        self.more_tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.more_tools_menu.add_command(label='Check GitHub', command=self.open_github)
        self.menu_bar.add_cascade(label='More Tools', menu=self.more_tools_menu)

        self.from_label = tk.Label(self.master, text='From:', font=('Arial', 12), bg='#ffcc00')
        self.from_label.place(x=50, y=50)

        self.from_currency_var = tk.StringVar()
        self.from_currency_menu = tk.OptionMenu(self.master, self.from_currency_var, "")
        self.from_currency_menu.config(font=('Arial', 10), width=15)
        self.from_currency_menu.place(x=120, y=50)

        self.to_label = tk.Label(self.master, text='To:', font=('Arial', 12), bg='#ffcc00')
        self.to_label.place(x=50, y=100)

        self.to_currency_var = tk.StringVar()
        self.to_currency_menu = tk.OptionMenu(self.master, self.to_currency_var, "")
        self.to_currency_menu.config(font=('Arial', 10), width=15)
        self.to_currency_menu.place(x=120, y=100)

        self.amount_label = tk.Label(self.master, text='Amount:', font=('Arial', 12), bg='#ffcc00')
        self.amount_label.place(x=50, y=150)

        self.amount_var = tk.StringVar()
        self.amount_entry = tk.Entry(self.master, textvariable=self.amount_var, font=('Arial', 12), width=15)
        self.amount_entry.place(x=120, y=150)

        self.convert_button = tk.Button(self.master, text='Convert', command=self.convert_currency, bg='#3498db', fg='white', font=('Arial', 12))
        self.convert_button.place(x=190, y=200)

        self.converted_label = tk.Label(self.master, text='Converted Amount:', font=('Arial', 12), bg='#ffcc00')
        self.converted_label.place(x=50, y=250)

        self.converted_amount_var = tk.StringVar()
        self.converted_amount_label = tk.Label(self.master, textvariable=self.converted_amount_var, font=('Arial', 12), bg='#ffcc00')
        self.converted_amount_label.place(x=200, y=250)

        self.get_currency_list()  

    def get_currency_list(self):
        try:
            api_key = 'API key Ko idhar dalneka'  
            url = f'https://open.er-api.com/v6/latest'
            response = requests.get(url, params={'apiKey': api_key})
            if response.status_code == 200:
                data = response.json()
                self.currency_list = data['rates']
                self.populate_currency_dropdown()
            else:
                messagebox.showerror('Error', 'Failed to fetch currency data.')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {str(e)}')

    def populate_currency_dropdown(self):
        currency_options = list(self.currency_list.keys())

        for currency in currency_options:
            self.from_currency_menu['menu'].add_command(label=currency, command=tk._setit(self.from_currency_var, currency))
            self.to_currency_menu['menu'].add_command(label=currency, command=tk._setit(self.to_currency_var, currency))

    def convert_currency(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.currency_list.get(self.from_currency_var.get())
            to_currency = self.currency_list.get(self.to_currency_var.get())

            if not from_currency or not to_currency:
                messagebox.showwarning('Warning', 'Select valid currencies.')
                return

            converted_amount = (amount / from_currency) * to_currency
            self.converted_amount_var.set(f'{converted_amount:.2f} {self.to_currency_var.get()}')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {str(e)}')

    def show_about(self):
        messagebox.showinfo('About', 'Currency Converter App\nVersion: 1.0\nDeveloped by: Ashutosh Palhare')

    def open_github(self):
        webbrowser.open_new("https://github.com/ashutosh786palhare")  

def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
