# Generated by Django 5.1.2 on 2024-11-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0009_remove_cart_product_remove_cart_user_items_item_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='items',
            name='item_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
