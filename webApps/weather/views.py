from django.shortcuts import render
import requests

from weather.models import City


def weather(request):
    appid = '44577d971869307d20581fa1c57234e3'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + appid

    cities = City.objects.all()

    all_cities = []
    # for city in cities:
    #     res = requests.get(url.format(city.name)).json()
    #     city_info = {
    #         'city': city.name,
    #         'temp': res["main"]["temp"],
    #         'icon': res["weather"][0]["icon"],
    #     }
    #     all_cities.append(city_info)

    data = {
        'all_info': all_cities
    }
    return render(request, 'weather/weather.html', data)
