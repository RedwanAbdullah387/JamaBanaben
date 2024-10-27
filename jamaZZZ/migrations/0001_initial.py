# Generated by Django 5.0.3 on 2024-10-26 20:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_name', models.CharField(max_length=200)),
                ('design_description', models.TextField(blank=True, null=True)),
                ('design_pic', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('design_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('item_pic', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('item_price', models.FloatField()),
                ('item_category', models.CharField(max_length=200)),
                ('item_stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('product_pic', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('product_price', models.FloatField()),
                ('product_category', models.CharField(max_length=200)),
                ('product_stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('type_of_product', models.CharField(blank=True, choices=[('Men', 'Men'), ('Women', 'Women')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jamaZZZ.product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('user_profile_pic', models.ImageField(blank=True, default='../upload/Default_pic.png', null=True, upload_to='upload')),
                ('type_of_user', models.CharField(blank=True, choices=[('normal', 'normal'), ('designer', 'designer')], max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
