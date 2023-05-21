from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse


class User(AbstractBaseUser):
    username = None

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=30)

    email = models.EmailField(max_length=254, unique=True)
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=80)
    phoneNumber = models.DecimalField(
        decimal_places=0, max_digits=9, null=True)
    USERNAME_FIELD = 'email'
    type = models.CharField(editable=False, max_length=10, default="myuser")