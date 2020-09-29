from django.shortcuts import render
from .models import Buyercost
# Create your views here.

def buyercost(request):
    all_buyerCost=Buyercost.objects.all()

    context={
        'buyercostlist':all_buyerCost
    }


    return  render(request,'Buyercost/buyercostinfo.html',context)



