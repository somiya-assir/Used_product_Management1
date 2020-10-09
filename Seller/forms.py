from django import forms
from .models import Seller

class SellerInput(forms.ModelForm):
    class Meta:
        model=Seller
        fields=['seller_name' , 'email','address','contact','details']


