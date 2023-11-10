import requests
from django.shortcuts import render
from currency_converter.forms import ConverterForm


def index(request):
    res = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = res.get('rates')
    if request.method == 'GET':
        data = {
            'currencies': currencies
        }
        return render(request, 'currency_converter/converter.html', data)
    if request.method == 'POST':
        print('Hello World')
        fromAmount = request.POST.get('fromAmount')
        fromCurr = request.POST.get('fromCurr')
        toCurr = request.POST.get('toCurr')
        res = round(currencies[toCurr] / currencies[fromCurr] * float(fromAmount),2)
        res = str(res).replace('.', ',')
        data = {
            'currencies': currencies,
            'fromAmount': fromAmount,
            'fromCurr': fromCurr,
            'toCurr': toCurr,
            'res': res,
        }
        return render(request, 'currency_converter/converter.html', data)