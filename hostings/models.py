from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from django.utils import timezone


class OpportunityModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Opportunity")
        verbose_name_plural = _("Opportunities")


class HostingModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    short_description = models.CharField(max_length=255, verbose_name=_("Short description"))
    price = models.FloatField(verbose_name=_("Price"))
    real_price = models.FloatField(verbose_name=_("Real price"), default=0)
    sale = models.BooleanField(verbose_name=_("Sale"), default=False)
    discount = models.PositiveSmallIntegerField(verbose_name=_("Discount"), default=0)
    opportunity = models.ManyToManyField(OpportunityModel, related_name='hosting', verbose_name=_("Opportunity"))
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)

    def is_discount(self):
        return bool(self.discount)

    def new(self):
        return (timezone.now() - self.created_at).days <= 5

    @staticmethod
    def get_cart_info(request):
        cart = request.session.get('cart', [])
        if not cart:
            return 0, 0.0
        return len(cart), HostingModel.objects.filter(id__in=cart).aggregate(Sum('real_price'))['real_price__sum']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Hosting")
        verbose_name_plural = _("List of hosting")
