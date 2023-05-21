from django.db import models
from Company.models import Company
import datetime
from dateutil.relativedelta import relativedelta
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
 
    @property
    def getPhone(self):
        return self.company.phoneNumber

    def getEmail(self):
        return self.company.email

    def expireDate(self):
        date_now = datetime.date.today()
        return date_now + relativedelta(months=1)

    def __str__(self):
        return "{} | {} | {}".format(self.title, self.position, self.company)

    def get_absolute_url(self):
        return reverse("detail-offer", kwargs={"pk": self.pk})


class OfferResponse(models.Model):
    offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=11)
    email = models.EmailField()
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=False, verbose_name=u"Your CV" )
    experience = models.DecimalField(max_digits = 3, decimal_places = 1, blank = True, null = True )
    education = models.CharField(max_length=50, blank = True, null = True)    #wyksztalcenie
    knownLanguages = models.CharField(max_length=255, blank = True, null = True)

    def __str__(self):
        return "{} offer to {}".format(self.user.name, self.offer.title)
