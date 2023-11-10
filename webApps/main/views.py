from django.shortcuts import render

def index(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/about.html')
