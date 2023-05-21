from django.contrib import admin
from .models import SimpleUser


@admin.register(SimpleUser)
class SimpleUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'viewFirstName', 'viewLastName')
    list_display_links = ('email', 'viewFirstName')
    ordering = ('email',)
    list_filter = ('is_staff', 'is_superuser', 'city', 'zipcode')
    search_fields = ('email', 'name', 'lastname', 'city', 'zipcode')

    fieldsets = (
        ('Basic', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('password', 'email')
        }),
        ('Additionally', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('name', 'lastname'), 'phoneNumber', ('zipcode', 'city', 'address'))
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
