from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomerAccount, Trader


@receiver(post_save, sender=Trader)
def create_trader_profile(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to our website',
            f"Thank you for using our website.😃 , {instance.full_name}!",
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
            )


@receiver(post_save, sender=CustomerAccount)
def create_customeraccount_profile(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to our website',
            f"Thank you for using our website.😃 , {instance.full_name}!",
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
            )
