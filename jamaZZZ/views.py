from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    items = Items.objects.all()
    context ={
        'item':  items,
    }
    return render(request,template_name='home.html',context=context)


# products
def women(request):
    wo = Product.objects.all()
    context ={
        'won':  wo,
    }
    return render(request,template_name='women.html',context=context)

def men(request):
    return render(request,template_name='men.html')





# designer page
def designer(request):
    return render(request, template_name='designer.html')


# cart page
def cart(request):
    return render(request,template_name='cart.html')

# contact_us page
def contact(request):
    return render(request,template_name='contact_us.html')

