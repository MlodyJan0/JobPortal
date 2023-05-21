from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'nip')
    list_display_links = ('email', 'name')
    ordering = ('email',)
    list_filter = ('is_staff', 'is_superuser', 'city', 'zipcode')
    search_fields = ('email', 'name', 'city', 'zipcode', 'nip')

    fieldsets = (
        ('Basic', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('password', 'email'), 'nip')
        }),
        ('Additionally', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'phoneNumber', ('zipcode', 'city', 'address'))
        }),
        ('Advanced options', {
            'classes': ('collapse'),
            'fields': ('is_staff', 'is_superuser'),
        }),
    )

    @admin.display(empty_value='empty', description='lastname')
    def viewLastName(self, obj):
        return obj.lastname

    @admin.display(empty_value='???', description='firstname')
    def viewFirstName(self, obj):
        return obj.name
