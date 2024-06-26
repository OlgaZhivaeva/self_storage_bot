from django.db import models

class Client(models.Model):
    name = models.CharField('ФИО', max_length=200)
    email = models.EmailField('email', unique=True)

    def __str__(self):
        return self.name


class Box(models.Model):
    start_storage = models.DateTimeField('начало хранения')
    end_storage = models.DateTimeField('конец хранения')
    client = models.ForeignKey(Client,
                               verbose_name='клиент',
                                on_delete=models.CASCADE,
                                related_name='boxes')

    def __str__(self):
        return f'арендован {self.client}'
