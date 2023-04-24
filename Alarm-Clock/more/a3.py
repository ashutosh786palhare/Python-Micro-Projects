from tkinter import *
import datetime
import time
import winsound

class AlarmClock:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")

        self.alarm_set = False

        # Create hour selection widget
        Label(master, text="Hour:").grid(row=0, column=0)
        self.hour_var = StringVar(master)
        self.hour_var.set("00")
        self.hour_menu = OptionMenu(master, self.hour_var, *range(0, 24))
        self.hour_menu.grid(row=0, column=1)

        # Create minute selection widget
        Label(master, text="Minute:").grid(row=1, column=0)
        self.min_var = StringVar(master)
        self.min_var.set("00")
        self.min_menu = OptionMenu(master, self.min_var, *range(0, 60))
        self.min_menu.grid(row=1, column=1)

        # Create second selection widget
        Label(master, text="Second:").grid(row=2, column=0)
        self.sec_var = StringVar(master)
        self.sec_var.set("00")
        self.sec_menu = OptionMenu(master, self.sec_var, *range(0, 60))
        self.sec_menu.grid(row=2, column=1)

        # Create set alarm button
        Button(master, text="Set Alarm", command=self.set_alarm).grid(row=3, column=0)

        # Create stop alarm button
        self.stop_button = Button(master, text="Stop Alarm", state=DISABLED, command=self.stop_alarm)
        self.stop_button.grid(row=3, column=1)

    def set_alarm(self):
        self.alarm_set = True
        self.hour_menu.configure(state=DISABLED)
        self.min_menu.configure(state=DISABLED)
        self.sec_menu.configure(state=DISABLED)

        while self.alarm_set:
            # Get the current time
            now = datetime.datetime.now()

            # Get the time at which the alarm should go off
            alarm_time = datetime.time(hour=int(self.hour_var.get()), minute=int(self.min_var.get()), second=int(self.sec_var.get()))

            # If the alarm time is the current time, play the alarm sound and disable the set alarm button
            if now.time() >= alarm_time:
                winsound.PlaySound("tone.mp3", winsound.SND_ASYNC | winsound.SND_LOOP)
                self.stop_button.configure(state=NORMAL)

            # Wait for one second before checking the time again
            time.sleep(1)

    def stop_alarm(self):
        self.alarm_set = False
        self.hour_menu.configure(state=NORMAL)
        self.min_menu.configure(state=NORMAL)
        self.sec_menu.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)
        winsound.PlaySound(None, 0)

root = Tk()
clock = AlarmClock(root)
root.mainloop()
