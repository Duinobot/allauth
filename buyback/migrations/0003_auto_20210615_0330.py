# Generated by Django 3.2.4 on 2021-06-15 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyback', '0002_sendlist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('confirmed', models.BooleanField(default=False)),
                ('exchange_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyback.exchange')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuybackItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('confirmed', models.BooleanField(default=False)),
                ('buyback_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyback.buyback')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='sendlist',
            name='buyback_items',
            field=models.ManyToManyField(blank=True, to='buyback.BuybackItem', verbose_name='BuyBack'),
        ),
        migrations.AlterField(
            model_name='sendlist',
            name='exchange_items',
            field=models.ManyToManyField(blank=True, to='buyback.ExchangeItem', verbose_name='Exchange'),
        ),
    ]
