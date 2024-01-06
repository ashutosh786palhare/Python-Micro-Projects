import tkinter as tk
from tkinter import messagebox
import random
import string
import webbrowser

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Password Generator by AP')
        self.master.geometry('470x550')  
        self.master.configure(bg='#f0f0f0')  
        self.password_history = []

        self.menu_bar = tk.Menu(master)
        self.master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Exit', command=self.exit_app)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label='About', command=self.show_about)
        self.menu_bar.add_cascade(label='About', menu=self.about_menu)

        self.more_tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.more_tools_menu.add_command(label='Check GitHub', command=self.open_github)
        self.menu_bar.add_cascade(label='More Tools', menu=self.more_tools_menu)

        self.password_label = tk.Label(self.master, text='Generated Password:', font=('Arial', 12), bg='#f0f0f0')
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.master, font=('Arial', 12), width=30)
        self.password_entry.pack(pady=5)

        self.generate_button = tk.Button(self.master, text='Generate Password', command=self.generate_password, bg='#3498db', fg='white')  
        self.generate_button.pack(pady=10)

        self.copy_button = tk.Button(self.master, text='Copy to Clipboard', command=self.copy_password, bg='#2ecc71', fg='white') 
        self.copy_button.pack(pady=5)

        self.history_button = tk.Button(self.master, text='History', command=self.display_history, bg='#9b59b6', fg='white')  
        self.history_button.pack(pady=5)

        self.length_label = tk.Label(self.master, text='Password Length:', bg='#f0f0f0')
        self.length_label.pack(pady=5)

        self.length_var = tk.IntVar()
        self.length_var.set(12)
        self.length_entry = tk.Entry(self.master, textvariable=self.length_var, font=('Arial', 12), width=10)
        self.length_entry.pack()

        self.lower_var = tk.IntVar()
        self.lower_check = tk.Checkbutton(self.master, text='Include Lowercase', variable=self.lower_var, bg='#f0f0f0')
        self.lower_check.pack()

        self.upper_var = tk.IntVar()
        self.upper_check = tk.Checkbutton(self.master, text='Include Uppercase', variable=self.upper_var, bg='#f0f0f0')
        self.upper_check.pack()

        self.digits_var = tk.IntVar()
        self.digits_check = tk.Checkbutton(self.master, text='Include Digits', variable=self.digits_var, bg='#f0f0f0')
        self.digits_check.pack()

        self.symbols_var = tk.IntVar()
        self.symbols_check = tk.Checkbutton(self.master, text='Include Symbols', variable=self.symbols_var, bg='#f0f0f0')
        self.symbols_check.pack()

    def generate_password(self):
        length = self.length_var.get()
        use_lower = self.lower_var.get()
        use_upper = self.upper_var.get()
        use_digits = self.digits_var.get()
        use_symbols = self.symbols_var.get()

        if not any([use_lower, use_upper, use_digits, use_symbols]):
            messagebox.showwarning('Warning', 'Please select at least one character type.')
            return

        characters = ''
        if use_lower:
            characters += string.ascii_lowercase
        if use_upper:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        generated_password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, generated_password)
        self.password_history.append(generated_password)

    def copy_password(self):
        password = self.password_entry.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            messagebox.showinfo('Success', 'Password copied to clipboard!')

    def display_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title('Password History')

        history_label = tk.Label(history_window, text='Generated Password History:', font=('Arial', 12))
        history_label.pack(pady=10)

        history_listbox = tk.Listbox(history_window, font=('Arial', 10), width=40, height=10)
        history_listbox.pack(pady=5)

        for password in self.password_history:
            history_listbox.insert(tk.END, password)

    def exit_app(self):
        self.master.destroy()

    def show_about(self):
        messagebox.showinfo('About', 'Password Generator App\nVersion: 1.0\nDeveloped by: Ashutosh Palhare')

    def open_github(self):
        webbrowser.open_new("https://github.com/ashutosh786palhare")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
