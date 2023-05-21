from django.contrib import admin

from .models import JobOffer
from .models import Category

admin.site.register(JobOffer)
admin.site.register(Category)