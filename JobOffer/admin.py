from django.contrib import admin

from .models import JobOffer, Category, OfferResponse

admin.site.register(OfferResponse)


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('company', 'category', 'position', 'isActive')
    list_display_links = ('company', 'position')
    ordering = ('company',)
    list_filter = ('company', 'category', 'position', 'isActive')
    search_fields = ('title', 'category', 'position')

    fieldsets = (
        ('Basic', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('title', ('position', 'category'))
        }),
        ('More information', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('company', 'description', 'wantEducation', 'wantExperience', 'wantLanguages')
        })
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)
