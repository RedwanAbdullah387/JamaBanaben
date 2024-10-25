from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,template_name='home.html')


# products page
def products(request):
    return render(request, template_name='products.html')


# designer page
def designer(request):
    return render(request, template_name='designer.html')


# cart page
def cart(request):
    return render(request,template_name='cart.html')

