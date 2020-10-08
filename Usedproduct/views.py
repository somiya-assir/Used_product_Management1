from django.shortcuts import render, redirect, get_object_or_404
from .models import Usedproduct
from .forms import ProductInput
from .models import Seller
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
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
        'form': form
    }
    return render(request, 'usedproduct/insertproduct.html', context)


def showDetails(request, product_id):
    searched_info = get_object_or_404(Usedproduct, id=product_id)
    context = {
        'search': searched_info
    }
    return render(request, 'usedproduct/showproductdetails.html', context)
