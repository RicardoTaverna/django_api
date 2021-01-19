from django.db import models


class ContactsMacapa(models.Model):
    name = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class ContactsVarejao(models.Model):
    name = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=13)

    def __str__(self):
        return self.title