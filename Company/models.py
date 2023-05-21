from django.db import models
from django.urls import reverse

from User.models import User


class Company(User):
    nip = models.DecimalField(unique=True, decimal_places=0, max_digits=10)

    def __init__(self, *args, **kwargs):
        self._meta.get_field("type").default = "company"
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name