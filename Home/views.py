
from django.shortcuts import render, redirect, get_object_or_404

def showhome(request):

    return  render(request,'home/home.html')



def showpricelist(request):

    return  render(request,'home/pricelist.html')
