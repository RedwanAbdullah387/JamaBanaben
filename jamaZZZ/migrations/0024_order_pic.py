# Generated by Django 5.1.2 on 2024-11-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0023_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pic',
            field=models.ImageField(blank=True, default='images/Default_pic.jpg', null=True, upload_to='images/'),
        ),
    ]
