# Generated by Django 5.1.2 on 2024-11-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0025_remove_order_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='p_quantity',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]