from django.urls import path
from .views import (AllOffersView, DetailOfferView, UpdateOfferView, DeleteOfferView, CategoryView, MyOffersView, addResponseToOffer, ListOfResponsesFor, addOfferView)


urlpatterns = [
    path('', AllOffersView.as_view(), name='all-offers'),
    path('<int:pk>', DetailOfferView.as_view(), name='detail-offer'),
    # path('add', AddOfferView.as_view(), name='add-offer'),
    path('add', addOfferView, name='add-offer'),
    path('<int:pk>/edit', UpdateOfferView.as_view(), name='update-offer'),
    path('<int:pk>/delete', DeleteOfferView.as_view(), name='delete-offer'),
    path('allMyOffers', MyOffersView, name='my-offers'),
    path('category/<str:category>', CategoryView, name='detail-category'),
    path('<int:pk>/response/add', addResponseToOffer, name='add-response'),
    path('<int:pk>/response', ListOfResponsesFor, name='list-response'),
]
