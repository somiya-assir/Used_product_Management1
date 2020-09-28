from django.shortcuts import render

from .models import Buyer


def buyerinfo(request):
    all_buyer=Buyer.objects.all()
    context={
        'buyerlist':all_buyer
    }

    return render(request,'Buyer/buyerinfo.html',context)