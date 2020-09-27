from django.db import models



from Seller.models import Seller
from Employee.models import Employee


# Create your models here.
class Pickup(models.Model):
    Shedule=models.TimeField()
    seller= models.ForeignKey(Seller, on_delete=models.CASCADE, default=1, null=True)
    employee_name=models.ForeignKey(Employee, on_delete=models.SET_NULL, default=1, null=True)
