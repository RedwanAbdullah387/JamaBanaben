# Generated by Django 5.1.2 on 2024-10-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0005_alter_items_item_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design_pic',
            field=models.ImageField(blank=True, default='../upload/Default_pic.png', null=True, upload_to='images/'),
        ),
    ]
