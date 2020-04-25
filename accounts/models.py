from django.db import models
from django.contrib.auth.models import User

class Phone(models.Model):

    number = models.CharField('страна', max_length=250)
    create_date = models.DateTimeField('дата загрузки ', auto_now_add=True)
    upload_date = models.DateTimeField('дата обновления ', auto_now=True)
    is_active = models.BooleanField('номер активен?')

    def __str__(self):
        return '{0}'.format(self.number)

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"

class Address(models.Model):

    country = models.CharField('страна', max_length=250)
    street = models.CharField('улица', max_length=250)
    house = models.CharField('дом', max_length=250)
    apartment = models.CharField('квартира', max_length=250)
    create_date = models.DateTimeField('дата загрузки ', auto_now_add=True)
    upload_date = models.DateTimeField('дата обновления ', auto_now=True)
    is_active = models.BooleanField('адресс актуален?')

    def __str__(self):
        return '{0}'.format(self.street)

    class Meta:
        verbose_name = "Адресс"
        verbose_name_plural = "Адресса"

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField('имя', max_length=250)
    lastname = models.CharField('фамилия', max_length=250)
    adddress = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.firstname)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"


