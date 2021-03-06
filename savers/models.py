from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False , blank=True)
    app_name = models.CharField(max_length=30, blank=True, null=True) 
    Email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12,null=True,blank=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100 , blank=False, null=False)

    def __str__(self):
        return self.app_name

