from django.shortcuts import render
from .models import Pickup
from .forms import Pickupinsertform
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def pickUp(request):
    all_pickup=Pickup.objects.all()

    context={
        'pickuplist':all_pickup
    }

    return render(request,'pickup/pickinfo.html',context)
@login_required
def insertpickup(request):
    form=Pickupinsertform()
    msg="seller information "

    if request.method=="POST":
        form=Pickupinsertform(request.POST)
        #msg="not successful"
        if form.is_valid():
          form.save()
          form=Pickupinsertform()
          msg="successfull🎈"


    context={
        'form':form,
        'msg':msg

    }

    return  render (request,'pickup/insertpickup.html',context)






