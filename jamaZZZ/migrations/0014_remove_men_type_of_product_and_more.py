# Generated by Django 5.1.2 on 2024-11-13 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0013_rename_item_id_items_id_rename_product_id_men_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='men',
            name='type_of_product',
        ),
        migrations.RemoveField(
            model_name='productwomen',
            name='type_of_product',
        ),
    ]
