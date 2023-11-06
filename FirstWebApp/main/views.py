from django.shortcuts import render

def index(request):
    data = {
        'title': 'Home page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')