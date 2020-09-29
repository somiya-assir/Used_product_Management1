from django.shortcuts import render
from .models import Employee

# Create your views here.
def employee(request):
    all_employee=Employee.objects.all()

    context={
        'employeelist':all_employee
    }

    return render(request,'Employee/employeeinfo.html',context)

