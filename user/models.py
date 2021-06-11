from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

CUSTOMER_GROUP_CHOICES = (
    ('business', 'Business'),
    ('platinum', 'Platinum'),
    ('vvip', 'VVIP'),
    ('wholesale', 'Wholesale'),
)


class Customer(AbstractUser):
    group = models.CharField(
        _("Customer Group"), default='business', choices=CUSTOMER_GROUP_CHOICES)
