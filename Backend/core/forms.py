# core/forms.py
from django import forms
from .models import NewsEvent

class NewsEventForm(forms.ModelForm):
    class Meta:
        model = NewsEvent
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format='%a, %d %b %Y', attrs={
                'type': 'date'
            }),
        }
