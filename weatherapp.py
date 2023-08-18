from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
    
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # Weather
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    api = f"https://api.openweathermap.org/data/2.5/weather?q="+city+"&12de483629997c883da58d4c2c7ad39b"

    json_data = requests.get(api).json()
    condition = json_data['WEATHER'][0]['main']
    description = json_data['WEATHER'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    T.config(text=(temp, "°"))
    C.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

    # Update other labels
    W.config(text=wind)
    H.config(text=humidity)
    D.config(text=description)
    P.config(text=pressure)


#search box
Search_image=PhotoImage(file="Copy of search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center", width=17, font=("poppins", 25, "bold"),bg="#404040", border=0, fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="Copy of search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
Logo_image=PhotoImage(file="Copy of logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image=PhotoImage(file="Copy of box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#Time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#Label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=270,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=450,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=670,y=400)

T=Label(font=("arial",70,"bold"),fg="#ee666d")
T.place(x=400,y=150)
C=Label(font=("arial",15,"bold"))
C.place(x=400,y=250)

W=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
W.place(x=130,y=430)
H=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
H.place(x=300,y=430)
D=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
D.place(x=500,y=430)
P=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
P.place(x=720,y=430)




root.mainloop()