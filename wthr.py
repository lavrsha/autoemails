# the goal of this project is to create a small desktop weather app using requests
import requests
from tkinter import *
from datetime import datetime

root = Tk()


def get_weather():
    city = str(cityField.get())
    countrycode = str(countryField.get())
    key = '84545b972c53550df96ee3361916d883'
    url = 'https://api.openweathermap.org/data/3.0/onecall'
    urlg = 'http://api.openweathermap.org/geo/1.0/direct'
    parms = {'q': [city, countrycode], 'appid': key}
    data = requests.get(urlg, params=parms)
    coords = data.json()
    lats = coords[0]['lat']
    lons = coords[0]['lon']
    params = {'appid': key, 'lat': lats, 'lon': lons, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(city)}: {weather["current"]["weather"][0]["main"], weather["current"]["temp"]}'


root.title('Weather app')
root.geometry('300x250')
root.resizable(width=False, height=False)

label = Label(root, text='Write your city and country code', font=30)
label.place(x=45, y=10)

frame_top = Frame(root, bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30, width=9)
cityField.place(x=5, y=0.1)

countryField = Entry(frame_top, bg='white', font=30, width=9)
countryField.place(x=104, y=0.1)

btn = Button(frame_top, text='Check the weather', command=get_weather)
btn.place(x=40, y=30)

info = Label(frame_bottom, text='Weather info', font=40)
info.pack()

now = datetime.now()
tme = Label(root, text = now.strftime('%d-%m-%Y , %H:%M'), font = 30, bg = 'white')
tme.place(x=80, y=200)


root.mainloop()
