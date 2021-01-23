import requests
import datetime
from config import variables


city_id = 550280
app_id = variables['APP_ID']
months = ["Января", "Ферваля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа",
          "Сентября", "Октября", "Ноября", "Декабря"]


def get_weather():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'appid': app_id, 'lang': 'ru', 'units': 'metric'})
        data = res.json()
        result = {
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'pressure': int(data['main']['pressure'] * 0.75),
            'humidity': data['main']['humidity'],
            'sunset': datetime.datetime.fromtimestamp(data['sys']['sunset']),
            'date': datetime.datetime.fromtimestamp(data['dt']),
            'wind': data['wind']
        }

        return result
    except Exception as e:
        print("Exception (find):", e)
