from django.db import models
from Buyer.models import Buyer
from Seller.models import Seller
# Create your models here.
class Usedproduct(models.Model):


    product_type=models.CharField(max_length=100)
    weight=models.IntegerField(blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, default=1, null=True)
    Buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, default=1, null=True, blank=True)


    def __str__(self):
        return self.product_type

