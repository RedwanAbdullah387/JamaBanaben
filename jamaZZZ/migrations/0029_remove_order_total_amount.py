# Generated by Django 5.1.2 on 2024-11-23 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0028_order_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
    ]