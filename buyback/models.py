from user.models import Customer
from django.db import models
from django.forms.fields import CharField, DecimalField
from django.contrib.auth import get_user_model

import uuid

# Create your models here.


class Buyback(models.Model):

    name = models.CharField(_("Buyback Screen Model"), max_length=50)
    price = models.DecimalField(_(""), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = _("Buyback")
        verbose_name_plural = _("Buybacks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Buyback_detail", kwargs={"pk": self.pk})


class Exchange(models.Model):

    name = models.CharField(_("Buyback Screen Model"), max_length=50)
    price = DecimalField(_(""), max_digits=5, decimal_places=2)

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
    status = models.CharField(
        _("Status"), default='pending', choices=BUYBACK_STATUS_CHOICES)

    buyback_items = models.ManyToManyField(
        Buyback, blank=True, verbose_name=_("BuyBack"))

    exchange_items = models.ManyToManyField(
        Exchange, blank=True, verbose_name=_("Exchange"))

    user = models.ForeignKey(get_user_model(), null=True, blank=True)

    class Meta:
        verbose_name = _("SendList")
        verbose_name_plural = _("SendLists")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("SendList_detail", kwargs={"pk": self.id})
