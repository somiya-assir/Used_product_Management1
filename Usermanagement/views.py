from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def registration(request):
    form = UserCreationForm()


    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
         form.save()
         #return redirect('login')

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
            #return redirect('login')

    context = {
        'form' : form
    }
    return render(request, 'Usermanagement/createprofile.html', context)
