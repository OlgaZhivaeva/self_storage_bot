import os
from django.core.mail import send_mail
from django.conf import settings
from .models import Box

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock.settings')


def test_email():
    send_mail(
        'Test Subject',
        'Test message body',
        'olga.zhiv@yandex.ru',
        ['olga.zhiv@yandex.ru'],
        fail_silently=False,
    )


def reminder(APIView):
    boxes_in_storage = Box.objects.filter(status='in_storage')
    if boxes_in_storage:
        for box in boxes_in_storage:
            send_mail(

                # title:
                'напоминание',
                # message:
                f'конец срока хранения {box.end_storage}',
                # from:
                settings.EMAIL_ADMIN,
                # to:
                [box.client.email],
                fail_silently=False,
            )
            print(box.client.name)
            print(f'конец срока хранения {box.end_storage}')
            print(f'сообщение отправлено на {box.client.email}')



from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
