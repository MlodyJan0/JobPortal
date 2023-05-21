from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import Company
from .forms import CompanyForm, CustomCompanyCreationForm
from django.views import generic
from django.shortcuts import render


def CompanyDetails(request, pk):
    if request.user.id == pk:
        company_details = Company.objects.get(pk=request.user.pk)
        return render(request, 'companyDetails.html', {'company': company_details})
    return render(request, 'ForbiddenPage.html', {})


class UpdateCompanyView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'updateCompany.html'


class DeleteCompanyView(DeleteView):
    model = Company
    template_name = 'deleteCompany.html'
    success_url = reverse_lazy('all-companies')


class CompanyRegisterView(generic.CreateView):
    form_class = CustomCompanyCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
