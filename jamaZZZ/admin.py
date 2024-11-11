from django.contrib import admin
from .models import Profile, Items, ProductWomen, Men,Design, Cart

# Register your models here.
admin.site.register([Profile, Items, ProductWomen, Men,Design, Cart])
