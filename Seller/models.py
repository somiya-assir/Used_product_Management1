from django.db import models

# Create your models here.
class Seller(models.Model):
    seller_name=models.CharField(max_length=100)
    email=models.EmailField(blank=True, null=True)
    address=models.CharField(max_length=200)
    contact=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.seller_name
