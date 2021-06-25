from django.contrib import admin
from django.db.models.base import Model
from user.models import Customer
from django.db import models
from django.forms.fields import CharField, DateTimeField, DecimalField
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .utils import unique_order_id_generator
from django.db.models.signals import pre_save, post_save, post_init, pre_init
from django.dispatch import receiver


import uuid

# Create your models here.


class Buyback(models.Model):

    name = models.CharField(_("Buyback Screen Model"), max_length=50)
    price = models.DecimalField(
        _("Buyback Price"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = _("Buyback")
        verbose_name_plural = _("Buybacks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Buyback_detail", kwargs={"pk": self.pk})


class Exchange(models.Model):

    name = models.CharField(_("Buyback Screen Model"), max_length=50)
    price = models.DecimalField(
        _("Exchange Price"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = _("Exchange Screen Model")
        verbose_name_plural = _("Exchanges")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Exchange_detail", kwargs={"pk": self.pk})


BUYBACK_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('received', 'Received'),
    ('tested', 'Tested'),
    ('complete', 'Complete'),
)


class SendList(models.Model):

    id = models.UUIDField(_("Buyback ID"), primary_key=True,
                          default=uuid.uuid4, editable=False)

    order_id = models.CharField(max_length=120, blank=True)

    status = models.CharField(
        _("Status"), default='pending', choices=BUYBACK_STATUS_CHOICES, max_length=100)

    # buyback_items = models.ManyToManyField(
    #     BuybackItem, blank=True, verbose_name=_("BuyBack"))

    # exchange_items = models.ManyToManyField(
    #     ExchangeItem, blank=True, verbose_name=_("Exchange"))

    customer = models.ForeignKey(get_user_model(), null=True,
                                 blank=True, on_delete=models.SET_NULL, related_name="order")

    modifier = models.ForeignKey(get_user_model(), null=True,
                                 blank=True, on_delete=models.SET_NULL, related_name="modifier")

    created_date = models.DateTimeField(
        _("Date Created"), default=timezone.now)
    modified_date = models.DateTimeField(
        _("Date Modified"), default=timezone.now)

    class Meta:
        verbose_name = _("SendList")
        verbose_name_plural = _("SendLists")

    def __str__(self):
        return self.order_id

    def get_absolute_url(self):
        return reverse("SendList_detail", kwargs={"pk": self.order_id})

# Creating a random order number for Sendlist


@receiver(pre_save, sender=SendList)
def _pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


class BuybackItem(models.Model):
    sendlist = models.ForeignKey(SendList, null=True, on_delete=models.CASCADE)
    buyback_item = models.ForeignKey(Buyback, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.buyback_item.name}"


class ExchangeItem(models.Model):
    sendlist = models.ForeignKey(SendList, null=True, on_delete=models.CASCADE)
    exchange_item = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.exchange_item.name}"
