from .models import City
from django.forms import ModelForm, DateInput, TextInput, DateTimeInput, DateTimeField
from datetime import datetime, timezone
from time import gmtime, strftime


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'City...',
                'class': 'form-control form-control-lg',
                'id': 'exampleFormControlInput1'
            }),
        }


    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)

