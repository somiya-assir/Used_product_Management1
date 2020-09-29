from django.shortcuts import render
from .models import Pickup

# Create your views here.
def pickUp(request):
    all_pickup=Pickup.objects.all()

    context={
        'pickuplist':all_pickup
    }

    return render(request,'pickup/pickinfo.html',context)

