from django.shortcuts import render

from .models import Seller
from .forms import SellerInput
#Create your views here.
def showseller(request):
    alluser = Seller.objects.all()

    contex = {
        'userlist': alluser
    }
    return render(request, 'sellermanagement/sellerlist.html', contex)

def insertseller(request):
    form=SellerInput()

    context={
        'form':form
    }

    return  render (request,'sellermanagement/insertseller.html',context)



