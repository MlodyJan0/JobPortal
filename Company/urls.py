from django.urls import path
from .views import UpdateCompanyView, DeleteCompanyView, CompanyDetails

urlpatterns = [
    path('<int:pk>', CompanyDetails, name='detail-company'),
    path('<int:pk>/edit', UpdateCompanyView.as_view(), name='update-company'),
    path('<int:pk>/delete', DeleteCompanyView.as_view(), name='delete-company')
]
