import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title('To-Do List App By AP')
        self.master.geometry("470x550")  # Enlarging the window size
        self.tasks = []

        self.task_frame = tk.Frame(self.master, bg='#f6f6f6')
        self.task_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.task_entry = tk.Entry(self.task_frame, width=30, font=('Arial', 12))
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_task_button = tk.Button(self.task_frame, text='Add Task', command=self.add_task,
                                         font=('Arial', 10), bg='#52b788', fg='white', relief=tk.FLAT)
        self.add_task_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_frame_inner = tk.Frame(self.task_frame, bg='#f6f6f6')
        self.task_frame_inner.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        self.clear_completed_button = tk.Button(self.master, text='Clear Completed', command=self.clear_completed,
                                                font=('Arial', 10), bg='#e63946', fg='white', relief=tk.FLAT)
        self.clear_completed_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, False))
            self.update_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning('Warning', 'Task cannot be empty')

    def toggle_task(self, index):
        task_label = self.task_frame_inner.winfo_children()[index].winfo_children()[1]
        if self.tasks[index][1]:
            task_label.config(font=('Arial', 12))
            task_label.config(fg='#333333')
        else:
            task_label.config(font=('Arial', 12, 'strike'))
            task_label.config(fg='#888888')
        self.tasks[index] = (self.tasks[index][0], not self.tasks[index][1])

    def delete_task(self, index):
        del self.tasks[index]
        self.update_tasks()

    def clear_completed(self):
        self.tasks = [task for task in self.tasks if not task[1]]
        self.update_tasks()

    def update_tasks(self):
        for widget in self.task_frame_inner.winfo_children():
            widget.destroy()

        for index, (task, completed) in enumerate(self.tasks):
            task_frame = tk.Frame(self.task_frame_inner, bg='#f6f6f6')
            task_frame.grid(row=index, column=0, sticky='ew')

            checkbox = tk.Checkbutton(task_frame, command=lambda i=index: self.toggle_task(i),
                                      bg='#f6f6f6', activebackground='#f6f6f6', highlightthickness=0)
            checkbox.select() if completed else checkbox.deselect()
            checkbox.grid(row=0, column=0, padx=(5, 2))

            task_label = tk.Label(task_frame, text=task, bg='#f6f6f6', font=('Arial', 12))
            task_label.grid(row=0, column=1, padx=(0, 5))

            delete_button = tk.Button(task_frame, text='Delete', command=lambda i=index: self.delete_task(i),
                                      font=('Arial', 8), bg='#eb4d4b', fg='white', relief=tk.FLAT)
            delete_button.grid(row=0, column=2, padx=(0, 5))

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
