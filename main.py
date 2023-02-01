from tkinter import *
from datetime import datetime, timedelta

#My sized fonts
DEFAULT_FONT_STYLE = ("Arial", 14)
TIME_FONT_STYLE = ("Arial", 46)

#Colors that I use
WHITE = "#FFFFFF"
LIGHT_PURPLE = "#5764DD"
LIGHT_GRAY = "#F8F9FB"
GRAY = "#C8C8C8"
DARK_GRAY = "#38444B"

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Def of my functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def stop_time():    # functions who change the value of my bool
    global count_bool
    if count_bool:
        count_bool = False
    else:
        count_bool = True
        count_time()


def count_time():     # functions that count and put it in right form
    if count_bool:
        global current_time
        current_time += timedelta(seconds=1)
        string = current_time.strftime('%H:%M:%S')
        current_time_label.config(text=string)
        current_time_label.after(1000, count_time)
        if current_time.strftime("%H:%M:%S") == alarm_time.strftime("%H:%M:%S"):    # Test if current time = Alarm
            alarm()


def set_time():      # functions called on (Set Time) button
    global current_time
    global mode
    hour = int(hour_entry.get())
    minute = int(min_entry.get())
    second = int(sec_entry.get())
    current_time = current_time.replace(hour=hour, minute=minute, second=second)
    if mode == "AM":              
        if hour >= 12:
            current_time = current_time.replace(hour=(current_time.hour - 12) % 12) 
            mode = "PM"  
    elif mode == "PM":
        if hour <= 12:
            current_time = current_time.replace(hour=(current_time.hour) % 12) 
            mode ="AM" 

    mode_label.config(text=mode)
    string = current_time.strftime('%H:%M:%S')
    current_time_label.config(text=string)


def set_alarm():    # functions called on (Set Alarm) button
    global alarm_time
    global mode
    hour = int(alarm_hour_entry.get())
    minute = int(alarm_min_entry.get())
    second = int(alarm_sec_entry.get())
    alarm_time = alarm_time.replace(hour=hour, minute=minute, second=second)
    if hour >= 12:
        if mode == "PM":
            alarm_time = alarm_time.replace(hour=(alarm_time.hour - 12) % 24) 
        elif mode == "AM":
            mode = "24h"
    string = alarm_time.strftime('%H:%M:%S')
    alarm_info_label.config(text=string)
    mode_label.config(text=mode)

#Change style to red and display message for 5s 
def alarm():
    alarm_info_label.config(fg="red")
    alarm_info_label.config(text="DRIIIIIINGGGGG, Wake up !")
    alarm_info_label.after(5000, alarm_off)
    
#Change to default style alarm
def alarm_off():
    alarm_info_label.config(fg="black")
    alarm_info_label.config(text=f"{alarm_time.strftime('%H:%M:%S')}")


#Switch AM to PM or PM to AM
def mode_am_pm():
    global current_time
    global mode
    if mode == "24h":
        if current_time.hour >= 12:
            current_time = current_time.replace(hour=(current_time.hour-12) % 12)
            mode = "PM"
        else:
            current_time = current_time.replace(hour=(current_time.hour) % 12)
            mode = "AM"
    else:
        if mode == "AM":
            current_time = current_time.replace(hour=(current_time.hour) % 24)
            mode = "24h"
        else:
            current_time = current_time.replace(hour=(current_time.hour + 12) % 24)
            mode = "24h"      
    string = current_time.strftime('%H:%M:%S')
    current_time_label.config(text=string)
    mode_label.config(text=mode)


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

gui = Tk()
gui.resizable(False,False)
gui.title("Clock")

current_time = datetime.now()
alarm_time = datetime.now()
count_bool = True # Bool that allow me to stop counting
mode = "24h"

#Create my TOP Frame
current_time_L_frame = LabelFrame(gui , text="Current Time", font=DEFAULT_FONT_STYLE)
current_time_L_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Create an entry for the amount to convert
current_time_label = Label(current_time_L_frame, font=TIME_FONT_STYLE)
current_time_label.grid(row=1, column=1, padx=10, pady=20, sticky="nsew")

mode_label = Label(current_time_L_frame, font=TIME_FONT_STYLE)
mode_label.grid(row=1, column=2, padx=10, pady=20, sticky="nsew")
mode_label.config(text=mode)

Label(current_time_L_frame,text="Alarm Set At :").grid(row=2, column=0, padx=10)
alarm_info_label = Label(current_time_L_frame)
alarm_info_label.grid(row=3, column=1, padx=10, pady=20, sticky="nsew")

set_alarm_button = Button(current_time_L_frame, text="AM / PM", command=mode_am_pm)
set_alarm_button.grid(row=4, column=0, padx=40, pady=10, sticky="nsew")

stop_button = Button(current_time_L_frame, text="Start / Stop", command=stop_time)
stop_button.grid(row=4, column=2, padx=40, pady=10, sticky="nsew")


#Create my CENTER Frame
set_time_L_frame = LabelFrame(gui, text="Set Time", font=DEFAULT_FONT_STYLE)
set_time_L_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

Label(set_time_L_frame,text="Hours").grid(row=0, column=0, padx=10)
hour_entry = Entry(set_time_L_frame, font=DEFAULT_FONT_STYLE)
hour_entry.grid(row=1, column=0, pady=10, sticky="nsew")

Label(set_time_L_frame,text="Minutes").grid(row=0, column=1, padx=10)
min_entry = Entry(set_time_L_frame, font=DEFAULT_FONT_STYLE)
min_entry.grid(row=1, column=1, pady=10, sticky="nsew")

Label(set_time_L_frame,text="seconds").grid(row=0, column=2, padx=10)
sec_entry = Entry(set_time_L_frame, font=DEFAULT_FONT_STYLE)
sec_entry.grid(row=1, column=2, pady=10, sticky="nsew")

set_time_button = Button(set_time_L_frame, text="Set Time", command=set_time)
set_time_button.grid(row=3, column=1, pady=10, sticky="nsew")


#Create my BOTTOM Frame
set_alarm_L_frame = LabelFrame(gui, text="Set Alarm", font=DEFAULT_FONT_STYLE)
set_alarm_L_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

Label(set_alarm_L_frame,text="Hours").grid(row=0, column=0, padx=10)
alarm_hour_entry = Entry(set_alarm_L_frame, font=DEFAULT_FONT_STYLE)
alarm_hour_entry.grid(row=1, column=0, pady=10, sticky="nsew")

Label(set_alarm_L_frame,text="Minutes").grid(row=0, column=1, padx=10)
alarm_min_entry = Entry(set_alarm_L_frame, font=DEFAULT_FONT_STYLE)
alarm_min_entry.grid(row=1, column=1, pady=10, sticky="nsew")

Label(set_alarm_L_frame,text="seconds").grid(row=0, column=2, padx=10)
alarm_sec_entry = Entry(set_alarm_L_frame, font=DEFAULT_FONT_STYLE)
alarm_sec_entry.grid(row=1, column=2, pady=10, sticky="nsew")

set_alarm_button = Button(set_alarm_L_frame, text="Set Alarm", command=set_alarm)
set_alarm_button.grid(row=3, column=1, pady=10, sticky="nsew")

count_time()
gui.mainloop()