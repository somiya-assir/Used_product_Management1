from django.shortcuts import render, redirect, get_object_or_404
from .models import Usedproduct
from .forms import ProductInput
from django.contrib.auth.decorators import login_required

# Create your views here.
def showsproduct(request):
    alluser = Usedproduct.objects.all()

    contex = {
        'userlist': alluser
    }

    return render(request, 'usedproduct/showproduct.html', contex)

@login_required
def insertpoduct(request):
    form = ProductInput()

    if request.method == "POST":
        form = ProductInput(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductInput()

    context = {
        'form' : form
    }
    return render(request, 'usedproduct/insertproduct.html', context)

