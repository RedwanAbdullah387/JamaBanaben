# Generated by Django 5.1.2 on 2024-11-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0008_alter_product_product_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='items',
            name='item_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]