# Generated by Django 5.1.2 on 2024-11-10 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0012_men'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='item_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='men',
            old_name='product_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='productwomen',
            old_name='product_id',
            new_name='id',
        ),
    ]