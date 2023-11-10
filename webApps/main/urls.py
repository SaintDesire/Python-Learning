from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('todo',include('todo.urls')),
    path('weather', include('weather.urls')),
    path('converter', include('currency_converter.urls')),
]
