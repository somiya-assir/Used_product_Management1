from django.db import models

from Buyer.models import Buyer

# Create your models here.
class Payment(models.Model):
    amount_Type=models.CharField(max_length=100)
    amount=models.IntegerField()
    Buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, default=1, null=True)
    def __str__(self):
        return self.amount_Type
