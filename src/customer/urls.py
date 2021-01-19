from django.urls import path
from .views import contacts_add, contacts_macapa


urlpatterns = [
    path('contacts/', contacts_add),
    path('contacts/macapa/', contacts_macapa)
]