# Generated by Django 3.0.6 on 2020-05-31 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sicilianpizza',
            name='price_small',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]