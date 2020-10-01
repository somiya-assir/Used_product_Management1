from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    contact_no = models.CharField(max_length=20)
    pro_pic = models.ImageField(upload_to='images/profile', blank=True, null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)