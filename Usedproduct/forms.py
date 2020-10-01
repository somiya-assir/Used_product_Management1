from django import forms
from .models import Usedproduct


class ProductInput(forms.ModelForm):
    class Meta:
        model=Usedproduct
        fields = '__all__'
