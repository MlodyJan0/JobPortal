from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from Company.models import Company
from User.models import SimpleUser
from .models import JobOffer, OfferResponse
from .forms import JobOfferForm, OfferResponseForm

class AllOffersView(ListView):
    model = JobOffer
    template_name = 'offers/allOffers.html'
    ordering = ['-id']


class DetailOfferView(DetailView):
    model = JobOffer
    template_name = 'offers/detailOffer.html'


def addOfferView(request):
    if request.user.type != "company":
        return render(request, 'ForbiddenPage.html', {})

    form = JobOfferForm(request.POST)
    if form.is_valid():
        response = form.save(commit=False)
        response.company = request.user
        response.isActive = True
        response.save()
        return redirect('my-offers')

    context = {'form': form}

    return render(request, 'offers/addOffer.html', context)


class UpdateOfferView(UpdateView):
    model = JobOffer
    form_class = JobOfferForm
    template_name = 'offers/updateOffer.html'


class DeleteOfferView(DeleteView):
    model = JobOffer
    template_name = 'offers/deleteOffer.html'
    success_url = reverse_lazy('my-offers')


def CategoryView(request, category):
    offer_category = JobOffer.objects.filter(category=category)
    return render(request, 'offers/allOffers.html', {'object_list': offer_category})


def MyOffersView(request):
    if request.user.type == "company":
        offers = JobOffer.objects.filter(company=request.user)
        return render(request, 'offers/allOffers.html', {'object_list': offers, 'ifEdit': '1'})
    return render(request, 'ForbiddenPage.html', {})


def ListOfResponsesFor(request, pk):
    responses = OfferResponse.objects.filter(offer=JobOffer.objects.get(pk=pk))
    if responses:
        return render(request, 'offers/responseList.html', {'responses': responses})
    elif request.user.type != 'user':
        return render(request, 'offers/responseList.html')
    return render(request, 'ForbiddenPage.html', {})


def addResponseToOffer(request, pk):
    if request.user.type == "company":        
        return render(request, 'ForbiddenPage.html', {})
    form = OfferResponseForm(request.POST or None, request.FILES)

    # pdb.set_trace()
    if request.method == 'POST':
        if form.is_valid():
            obj = get_object_or_404(JobOffer, pk=pk)
            response = form.save(commit=False)
            response.offer = obj
            response.user = request.user
            response.lastName = SimpleUser.objects.get(
                email=request.user.email).lastname
            response.firstName = request.user.name
            response.phoneNumber = request.user.phoneNumber
            response.email = request.user.email
            response.save()

            return redirect(obj.get_absolute_url())
    object = JobOffer.objects.get(pk = pk)

    context = {'form': form, 'object':object}

    return render(request, 'offers/addResponse.html', context)
