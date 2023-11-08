from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('<int:pk>/delete', views.deleteCity, name='deleteCity'),
]
