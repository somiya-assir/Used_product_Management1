from django.shortcuts import render

from .models import Seller
from .forms import SellerInput
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======
>>>>>>> 3c9ea3bb729d961a3c4ea4997c6d7e3eea20332d
#Create your views here.
def showseller(request):
    alluser = Seller.objects.all()

    contex = {
        'userlist': alluser
    }
    return render(request, 'sellermanagement/sellerlist.html', contex)
@login_required
def insertseller(request):
    form=SellerInput()
    msg="seller information "

    if request.method=="POST":
        form=SellerInput(request.POST)
        #msg="not successful"
        if form.is_valid():
          form.save()
          form=SellerInput()
          msg="successfull🎈"


    context={
        'form':form,
        'msg':msg

    }

    return  render (request,'sellermanagement/insertseller.html',context)

def insertseller(request):
    form=SellerInput()

    context={
        'form':form
    }

    return  render (request,'sellermanagement/insertseller.html',context)



