from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    name = models.CharField('ФИО', max_length=200)
    email = models.EmailField('email', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Box(models.Model):
    start_storage = models.DateTimeField('начало хранения')
    end_storage = models.DateTimeField('конец хранения')
    client = models.ForeignKey(Client,
                               verbose_name='клиент',
                                on_delete=models.CASCADE,
                                related_name='boxes')

    def __str__(self):
        return f'бокс {self.id}'

    class Meta:
        verbose_name = 'Бокс'
        verbose_name_plural = 'Боксы'

class Order(models.Model):
    client = models.ForeignKey(Client,
                               verbose_name='клиент',
                                on_delete=models.CASCADE,
                                related_name='orders')
    address =models.TextField('адрес', null=True, blank=True)
    phone = PhoneNumberField('телефон', unique=True)
    box = models.OneToOneField(Box, on_delete = models.CASCADE)

    def __str__(self):
        return f'заказ {self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Stock(models.Model):
    name = models.CharField('название', max_length=200)
    address = models.TextField('адрес', null=True, blank=True)