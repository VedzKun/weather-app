import requests
import tkinter as tk
import ttkbootstrap as ttk

api_key = "##add your own api key here##"


def generate():
    display_var.set(entry_var.get())
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={entry_var.get()}&units=metric&appid={api_key}")
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    speed = weather_data.json()['wind']['speed']
    weather_var.set(weather)
    temp_var.set(temp)
    speed_var.set(speed)
    

window = ttk.Window(themename="superhero")
window.geometry('450x800')

temp_frame = ttk.Frame(master=window)


title_label= ttk.Label(master=window, text = "Weather App", font="Calibri 24")
title_label.pack(pady=65)

input_frame = ttk.Frame(master=window)
entry_var = ttk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_var)
button = ttk.Button(master=input_frame, text="Enter", command=generate)
input_frame.pack(padx=10,pady=11)
entry.pack(side="left",pady=11)
button.pack(side="left", padx=5)

display_var = ttk.StringVar()
display = ttk.Label(master=window, 
                    text= "gi", 
                    font= "Calibri 20", 
                    textvariable=display_var)
display.pack(pady=12)

weather_var = ttk.StringVar()

weather_info = ttk.Label(master=window, 
                         text="hi",
                         font="Caibri 15", 
                         textvariable=weather_var)
weather_info.pack(pady=9)

temp_var = ttk.StringVar()
temp_info = ttk.Label(master=window, 
                      text="hi", 
                      font="Calibri 15", 
                      textvariable=temp_var)
temp_info.pack(pady=9)

speed_var = ttk.StringVar()
speed_info = ttk.Label(master=window, 
                       text="hi", 
                       font = "Calibri 15", 
                       textvariable=speed_var)
speed_info.pack(pady=5)

#weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}")
#weather = weather_data.json()['weather'][0]['main']
#temp = weather_data.json()['main']['temp']
window.mainloop()
