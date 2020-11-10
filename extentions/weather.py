import requests

from extentions.funcs import speak


def weather():

    # Getting weather
    try:
        req = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Rehovot,Israel&units=metric&appid=TOKEN')
        x = req.json()

        main = x['main']
        temp = main['temp']
        speak(f"Today's weather temperature in Rehovot Israel is, {temp} celsius")

    except:
        speak('Cant tell the weather, please check my code.')
