from django.urls import path
from .views import BaseRegistrationUser
app_name = 'base_registration'

urlpatterns = [
    path('', BaseRegistrationUser.as_view())
    ]
