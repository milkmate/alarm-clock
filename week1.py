from datetime import datetime
import tkinter as tk
from tkinter import ttk
import winsound

def set_alarm():
    alarm_time = entry.get()
    current_time = datetime.now().strftime("%H:%M")
    remaining_minutes = calculate_remaining_time(current_time, alarm_time)
    update_timer_label(remaining_minutes)

def calculate_remaining_time(current_time, alarm_time):
    current_hour, current_minute = map(int, current_time.split(':'))
    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))

    current_total_minutes = current_hour * 60 + current_minute
    alarm_total_minutes = alarm_hour * 60 + alarm_minute

    if alarm_total_minutes >= current_total_minutes:
        remaining_minutes = alarm_total_minutes - current_total_minutes
    else:
        remaining_minutes = (24 * 60) - (current_total_minutes - alarm_total_minutes)

    return remaining_minutes

def update_timer_label(remaining_minutes):
    if remaining_minutes <= 0:
        timer_label.config(text="Alarm time reached \u23F0")
        play_alarm_sound()
    else:
        hours = remaining_minutes // 60
        minutes = remaining_minutes % 60
        timer_label.config(text="Time remaining: {:02d}:{:02d}".format(hours, minutes))

def play_alarm_sound():
    frequency = 2500  # Set the frequency (Hz)
    duration = 2000  # Set the duration (ms)
    winsound.Beep(frequency, duration)

def stop_alarm():
    timer_label.config(text="Alarm stopped")
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Python Alarm Clock")
window.geometry("400x200")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 12))

label = ttk.Label(window, text="Set alarm time (24-hour format):")
label.pack()

entry = ttk.Entry(window)
entry.pack()

set_button = ttk.Button(window, text="Set Alarm", command=set_alarm)
set_button.pack()

timer_label = ttk.Label(window, text="Time remaining: 00:00")
timer_label.pack()

stop_button = ttk.Button(window, text="Stop Alarm", command=stop_alarm)
stop_button.pack()

window.mainloop()
