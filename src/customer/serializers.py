from .models import ContactsMacapa, ContactsVarejao
from rest_framework import serializers


class ContactsMacapaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactsMacapa
        fields = ['name', 'cellphone']

class ContactsVarejaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactsVarejao
        fields = ['name', 'cellphone']