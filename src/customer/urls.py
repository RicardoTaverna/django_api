from django.urls import path
from .views import contacts_add


urlpatterns = [
    path('contacts/', contacts_add),
]