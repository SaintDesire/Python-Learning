from django.db.models import Subquery
from django.shortcuts import render, redirect
import requests
from weather.forms import CityForm
from weather.models import City


def weather(request):
    appid = '44577d971869307d20581fa1c57234e3'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + appid
    form = CityForm()

    cities = City.objects.all().order_by(f'-id')[:10]
    error = ''
    all_cities = []
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data["name"]
            res = requests.get(url.format(city_name)).json()
            if res["cod"] == 200:
                if City.objects.filter(name=city_name).exists() == False:
                    form.save()
                    return redirect('weather')
                else:
                    error = 'City is already on the list'
            else:
                error = "City not found in the external API"
        else:
            error = 'Error'

    total_cities = City.objects.count()
    if total_cities > 10:
        records_to_delete = total_cities - 10
        ids_to_delete = City.objects.order_by('id')[:records_to_delete].values('id')
        City.objects.filter(id__in=Subquery(ids_to_delete)).delete()

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        if res["cod"] == 200:
            if City.objects.filter(name=city.name).exists() == False:
                error = "City not found"
            if int(res["main"]["temp"]) > 0:
                temp = '+' + str(int(res["main"]["temp"]))
                city_info = {
                    'city': city.name,
                    'temp': temp,
                    'icon': res["weather"][0]["icon"],
                    'id': city.id
                }
                all_cities.append(city_info)



    data = {
        'all_info': all_cities,
        'error': error,
        'form': form
    }
    return render(request, 'weather/weather.html', data)

def deleteCity(request, pk):
    todo = City.objects.get(id=pk)
    todo.delete()
    return redirect('/weather')