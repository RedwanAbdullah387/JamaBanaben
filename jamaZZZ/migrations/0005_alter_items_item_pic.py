# Generated by Django 5.1.2 on 2024-10-31 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0004_alter_items_item_pic_alter_product_product_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_pic',
            field=models.ImageField(blank=True, default='../upload/Default_pic.jpg', null=True, upload_to='images/'),
        ),
    ]