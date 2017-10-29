from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', verbose_name='Uživatel')
    info = models.TextField('Poznámka', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name        = 'profil'
        verbose_name_plural = 'profily'


class Room(models.Model):
    name        = models.CharField('Název', max_length=100)
    description = models.TextField('Poznámka', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'Místnost'
        verbose_name_plural = 'Místnosti'

class Message(models.Model):
    message = models.TextField('Správa')
    user    = models.ForeignKey('UserProfile')
    room    = models.ForeignKey('Room')