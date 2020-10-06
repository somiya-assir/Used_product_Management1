from django.shortcuts import render
from .models import Sellercost
# Create your views here.

def showsellercost(request):
    all_buyerCost=Sellercost.objects.all()

    context={
        'buyercostlist':all_buyerCost
    }


    return  render(request,'Sellercost/sellercost.html',context)



