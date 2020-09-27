from django.db import models
from Employee.models import Employee
from Usedproduct.models import Usedproduct
# Create your models here.
class Buyercost(models.Model):

  amount=models.IntegerField()
  employee_name = models.ForeignKey(Employee, on_delete=models.SET_NULL, default=1, null=True)

  usedproduct = models.ForeignKey(Usedproduct, on_delete=models.CASCADE, default=1, null=True)

