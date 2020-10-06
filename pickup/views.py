from django.shortcuts import render
from .models import Pickup
from .forms import Pickupinsertform

# Create your views here.
def pickUp(request):
    all_pickup=Pickup.objects.all()

    context={
        'pickuplist':all_pickup
    }

    return render(request,'pickup/pickinfo.html',context)

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






