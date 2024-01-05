import tkinter as tk
import random

class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Dice Roller by AP')
        self.master.geometry('270x190')

        self.result_label = tk.Label(self.master, text='', font=('Arial', 20))
        self.result_label.pack(pady=20)

        self.roll_button = tk.Button(self.master, text='Roll Dice', command=self.roll_dice)
        self.roll_button.pack()

    def roll_dice(self):
        dice_value = random.randint(1, 6)  # Generating a random number between 1 and 6 for a standard six-sided die
        self.result_label.config(text=str(dice_value))

def main():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
