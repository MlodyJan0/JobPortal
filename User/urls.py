from django.urls import path, include
from .views import UserRegisterView, UpdateUserView
from Company.views import CompanyRegisterView

urlpatterns = [
    path('registerUser/', UserRegisterView.as_view(), name='register-user'),
    path('<int:pk>/edit/', UpdateUserView.as_view(), name='update-user'),
    path('registerCompany/', CompanyRegisterView.as_view(), name='register-company'),
    path('login/',  include('allauth.urls'))
]