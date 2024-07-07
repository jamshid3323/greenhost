from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import HostingModel


@receiver(pre_save, sender=HostingModel)
def get_real_price(sender, instance, *args, **kwargs):
    if instance.is_discount():
        instance.real_price = round(((100 - instance.discount) / 100) * instance.price, 2)
    else:
        instance.real_price = instance.price


@receiver(pre_save, sender=HostingModel)
def set_sale(sender, instance, *args, **kwargs):
    if instance.is_discount():
        instance.sale = True
    else:
        instance.sale = False
