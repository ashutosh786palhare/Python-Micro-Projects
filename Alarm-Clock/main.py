from tkinter import *
from datetime import datetime
import threading
import winsound

def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            winsound.PlaySound("alarm.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
            break

def start_alarm():
    global alarm_thread
    alarm_thread = threading.Thread(target=set_alarm)
    alarm_thread.start()

def stop_alarm():
    winsound.PlaySound(None, winsound.SND_ASYNC) # Stop playing the sound
    if alarm_thread.is_alive():
        alarm_thread.join() # Wait for the alarm thread to finish

root = Tk()
root.geometry("400x300")
root.title("AP")

time_label = Label(root, text="Set Alarm Time", font=("Helvetica", 14))
time_label.pack(pady=20)

time_frame = Frame(root)
time_frame.pack()

hour = StringVar(root)
hours = ["{:02d}".format(i) for i in range(24)]
hour.set(hours[0])

minute = StringVar(root)
minutes = ["{:02d}".format(i) for i in range(60)]
minute.set(minutes[0])

second = StringVar(root)
seconds = ["{:02d}".format(i) for i in range(60)]
second.set(seconds[0])

hour_menu = OptionMenu(time_frame, hour, *hours)
hour_menu.pack(side=LEFT)

minute_menu = OptionMenu(time_frame, minute, *minutes)
minute_menu.pack(side=LEFT)

second_menu = OptionMenu(time_frame, second, *seconds)
second_menu.pack(side=LEFT)

start_button = Button(root, text="Start", font=("Helvetica", 14), command=start_alarm)
start_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Helvetica", 14), command=stop_alarm)
stop_button.pack()

root.mainloop()
