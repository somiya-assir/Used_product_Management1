from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name=models.CharField(max_length=100)
    contact=models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True, null=True)
    def __str__(self):
        return self.employee_name

