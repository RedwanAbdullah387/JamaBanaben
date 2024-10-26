from django.contrib import admin
from .models import Profile, Items, Product, Design, Cart

# Register your models here.
admin.site.register([Profile, Items, Product, Design, Cart])
