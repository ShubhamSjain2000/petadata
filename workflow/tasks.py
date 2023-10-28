
from celery import shared_task
from django.core.mail import send_mail

from petadata.settings import EMAIL_HOST_USER
@shared_task
def async_send_mail(subject, body, emails):

    send_mail(subject, body, EMAIL_HOST_USER, emails)


