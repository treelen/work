from django.urls import path
from .views import Contacts

urlpatterns = [
    path('contact/',Contacts.as_view(),name='contact')
]
