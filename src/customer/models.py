from django.db import models


class ContactsMacapa(models.Model):
    """Modelo para a tabela de contatos da empresa Macapa."""
    name = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class ContactsVarejao(models.Model):
    """Modelo para a tabela de contatos da empresa Varejao."""
    name = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=13)

    def __str__(self):
        return self.title