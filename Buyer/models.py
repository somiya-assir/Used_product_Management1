from django.db import models

# Create your models here.
class Buyer(models.Model):
    buyer_name=models.CharField(max_length=100)
    contact_no = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.buyer_name
