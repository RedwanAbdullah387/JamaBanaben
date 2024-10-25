from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,template_name='home.html')


# products
def women(request):
    return render(request,template_name='women.html')

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

