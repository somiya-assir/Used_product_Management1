from django import forms
from .models import Pickup

class Pickupinsertform(forms.ModelForm):
    class Meta:
        model=Pickup
        fields=['Shedule']
