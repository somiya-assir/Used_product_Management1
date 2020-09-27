from django.shortcuts import render

from .models import Seller
#Create your views here.
def showseller(request):
    alluser = Seller.objects.all()

    contex = {
        'userlist': alluser
    }
    return render(request, 'sellermanagement/sellerlist.html', contex)



