from django import forms
from .models import Converter

class ConverterForm(forms.ModelForm):
    class Meta:
        model = Converter
        fields = ['fromAmount']

        widgets = {
            'fromAmount': forms.TextInput(attrs={
                'placeholder': 'fromAmount...',
                'class': 'form-control form-control-lg',
                'id': 'exampleFormControlInput1'
            })
        }
