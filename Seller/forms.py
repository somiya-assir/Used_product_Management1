from django import forms
from .models import Seller

class SellerInput(forms.ModelForm):
    class Meta:
        model=Seller
        fields=['seller_name' , 'email','address','contact']

<<<<<<< HEAD

=======
>>>>>>> 3c9ea3bb729d961a3c4ea4997c6d7e3eea20332d
