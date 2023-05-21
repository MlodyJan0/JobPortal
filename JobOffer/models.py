from django.db import models
from Company.models import Company
import datetime
from django.urls import reverse
from User.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("all-category")


class JobOffer(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    position = models.CharField(max_length=50)
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    dateOfListing = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=True)
    category = models.CharField(
        max_length=30, default='none')
    wantEducation = models.BooleanField(default=False)
    wantLanguages = models.BooleanField(default=False)
    wantExperience = models.BooleanField(default=False)