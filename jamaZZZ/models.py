from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Profile(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)

 user_mobile = models.CharField(max_length=11, null=True, blank=True)
 user_profile_pic = models.ImageField(upload_to='images/', null=True, blank=True, default='images/Default_pic.png')
            #need to include default_pic
 user_type = (
  ('normal', 'normal'),
  ('designer', 'designer')
 )
 type_of_user = models.CharField(max_length=10, choices=user_type, blank=True, null=True)

 def __str__(self):
  return self.user.username


class Items(models.Model):
 id = models.IntegerField(primary_key=True)
 item_name = models.CharField(max_length=200)
 item_description = models.TextField(blank=True, null=True)
 item_pic = models.ImageField(upload_to='images/', null=True, blank=True,default='images/Default_pic.jpg')
 item_price = models.FloatField()
 item_category = models.CharField(max_length=200)
 item_stock = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

 def __str__(self):
  return self.item_name


class ProductWomen(models.Model):
 id = models.IntegerField(primary_key=True)
 product_name = models.CharField(max_length=200)
 product_description = models.TextField(blank=True, null=True)
 product_pic = models.ImageField(upload_to='images/', null=True, blank=True,default='images/Default_pic.jpg')
 product_price = models.FloatField()
 product_category = models.CharField(max_length=200)
 product_stock = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
 product_type = (
  ('Men', 'Men'),
  ('Women', 'Women')
 )
 type_of_product = models.CharField(max_length=10, choices=product_type, blank=True, null=True)
 def __str__(self):
  return self.product_name


class Men(models.Model):
 id = models.IntegerField(primary_key=True)
 product_name = models.CharField(max_length=200)
 product_description = models.TextField(blank=True, null=True)
 product_pic = models.ImageField(upload_to='images/', null=True, blank=True,default='images/Default_pic.jpg')
 product_price = models.FloatField()
 product_category = models.CharField(max_length=200)
 product_stock = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
 product_type = (
  ('Men', 'Men'),
  ('Women', 'Women')
 )
 type_of_product = models.CharField(max_length=10, choices=product_type, blank=True, null=True)
 def __str__(self):
  return self.product_name


class Design(models.Model):
 design_name = models.CharField(max_length=200)
 design_description = models.TextField(blank=True, null=True)
 design_pic = models.ImageField(upload_to='images/', null=True, blank=True,default='images/Default_pic.png')
 design_price = models.FloatField()

 def __str__(self):
  return self.design_name


class Cart(models.Model):
 create_date = models.DateTimeField(auto_now_add= True, auto_now= False)
 update_date = models.DateTimeField(auto_now_add=True, auto_now=False)

