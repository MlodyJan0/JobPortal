from django import forms
from .models import Company
from django.contrib.auth.forms import UserCreationForm


class CustomCompanyCreationForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-field d-flex align-items-center', 'style':
                                                                  'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;', 'type': 'password',
                                                                  'name': 'password'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-field d-flex align-items-center', 'style':
                                                                  'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;', 'type': 'password',
                                                                  'name': 'password2'}), label='Password Confirmation')

    class Meta:
        model = Company
        fields = ('email', 'nip', 'name', 'zipcode', 'city', 'address', 'phoneNumber')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-field d-flex align-items-center', 'style':
                                            'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;'}),
            'nip': forms.TextInput(attrs={'class': 'form-field d-flex align-items-center', 'style':
                                          'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;'}),
            'name': forms.TextInput(attrs={'class': 'form-field d-flex align-items-center', 'style':
                                           'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-field d-flex align-items-center', 'style':
                                              'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;'}),
            'city': forms.TextInput(attrs={'class': 'form-field d-flex align-items-center', 'style':
                                           'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;'}),
            'address': forms.TextInput(attrs={'class': 'form-field d-flex align-items-center', 'style':
                                              'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-field d-flex align-items-center', 'style':
                                                  'width: 300px;height: 40px;font-size:20px; font-size:20px; display:block;margin-right: auto;margin-left: auto;'}),
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'email', 'nip', 'zipcode', 'city', 'address', 'phoneNumber')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
        }
