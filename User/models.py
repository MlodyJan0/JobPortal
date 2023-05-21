from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    objects = UserManager()
    
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

    def __str__(self):
        return "{} - {}".format(self.name, self.email)

    def get_absolute_url(self):
        return reverse("all-offers")


class SimpleUser(User):
    lastname = models.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        self._meta.get_field("type").default = "user"
        super().__init__(*args, **kwargs)