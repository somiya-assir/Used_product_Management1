from django.shortcuts import render

from .models import  Payment
# Create your views here.

def showpayment(request):
    all_pay=Payment.objects.all()
    context={
        'paymentlist':all_pay
    }

    return  render(request,'Payment/paymentinfo.html',context)
