from django import forms
from datetime import datetime as dt

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES=(
        
        ('C','Contact'),
        ('S','Sharing'),
        ('T','Team'),
        
    
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    vacancy = forms.DateTimeField(required=True, input_formats=['T%H:%M', ])
    book = forms.DateTimeField(required=True, input_formats=['T%H:%M', ])

   