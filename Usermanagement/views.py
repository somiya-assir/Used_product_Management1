#from django.shortcuts import render,redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def registration(request):
    form = UserCreationForm()


    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
         user=form.save(commit=False)
         user.is_active=False
         user.save()
         return redirect('login')

    context={
        'form':form
    }

    return render(request,'Usermanagement/registration.html',context)
@login_required
def create_profile(request):
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('view_profile')

    context = {
        'form' : form
    }
    return render(request, 'Usermanagement/createprofile.html', context)


@login_required
def view_profile(request):


    profile=Profile.objects.get(user=request.user)




    context = {
        'profile': profile
    }

    return render(request, 'UserManagement/viewprofile.html', context)
