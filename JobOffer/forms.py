from django import forms
from .models import JobOffer, Category, OfferResponse

class JobOfferForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="(Nothing)")
    wantEducation= forms.BooleanField(required= False, label = "Require education level")
    wantExperience= forms.BooleanField( required= False, label = "Require experience in profession")

    wantLanguages = forms.BooleanField( required= False, label = "Require known languages")
    class Meta:
        model = JobOffer
        fields = ('title', 'description', 'position', 'category','wantEducation','wantExperience','wantLanguages')
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'cols': 8}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'cols': 5}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),        

        }
  

class OfferResponseForm(forms.ModelForm):
    # category = forms.ModelChoiceField(
    #  queryset=Category.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = OfferResponse
        fields = ('description', 'experience','education', 'knownLanguages', 'file')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'cols': 5}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'cols': 5, 'required': 'False'}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'cols': 5, 'required': 'False'}),
            'knownLanguages': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'cols': 5, 'required': 'False'}),
        }

    
