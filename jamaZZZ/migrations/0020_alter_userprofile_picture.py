# Generated by Django 5.1.2 on 2024-11-23 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0019_userprofile_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='images/Default_pic.jpg', null=True, upload_to='images/'),
        ),
    ]