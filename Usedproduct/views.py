from django.shortcuts import render, redirect, get_object_or_404
from .models import Usedproduct
from .forms import ProductInput
from .models import Seller
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def showsproduct(request):
    alluser = Usedproduct.objects.all()

    if request.method == 'POST':
        alluser = Usedproduct.objects.filter(product_type__icontains= request.POST['search'])
        seller1=Usedproduct.objects.filter(id__icontains= request.POST['search'])

        alluser= alluser | seller1

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
        'form': form
    }
    return render(request, 'usedproduct/insertproduct.html', context)


def showDetails(request, product_id):
    searched_info = Usedproduct.objects.filter(id=product_id)
    if len(searched_info) == 0:
        does_exists = False
        context = {
            'does_exists': does_exists,
        }
    else:
        does_exists = True
        search =  searched_info[0]
        context = {
            'does_exists': does_exists,
            'search': search
        }

    return render(request, 'usedproduct/showproductdetails.html', context)
