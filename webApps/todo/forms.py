from .models import Todo
from django.forms import ModelForm, DateInput, TextInput, DateTimeInput, DateTimeField
from datetime import datetime, timezone
from time import gmtime, strftime


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'addDate', 'dueDate', 'status']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Task name...',
                'class': 'form-control form-control-lg',
                'id': 'exampleFormControlInput1'
            }),
        }


    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)

        self.fields['addDate'].widget = DateTimeInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        self.fields['addDate'].initial = datetime.now().date()
        self.fields['dueDate'].widget = DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        self.fields['dueDate'].initial = datetime.now()
        self.fields['status'].initial = False
