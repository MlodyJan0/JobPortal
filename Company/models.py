from django.db import models
from django.urls import reverse

from User.models import User


class Company(User):
    nip = models.DecimalField(unique=True, decimal_places=0, max_digits=10)
