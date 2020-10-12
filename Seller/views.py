
from django.shortcuts import render, redirect, get_object_or_404
from .models import Seller
from .forms import SellerInput

from django.contrib.auth.decorators import login_required

#Create your views here.
@login_required
def showseller(request):
    alluser = Seller.objects.all()

    contex = {
        'userlist': alluser
    }
    return render(request, 'sellermanagement/sellerlist.html', contex)
#@login_required

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
          return redirect('insertpickup')

    context={
        'form':form,
        'msg':msg

    }

    return  render (request,'sellermanagement/insertseller.html',context)



