from django.shortcuts import render,redirect
from .models import *
from .forms import ItemsForm


# Create your views here.

def home(request):
    items = Items.objects.all()
    context ={
        'item':  items,
    }
    return render(request,template_name='home.html',context=context)

def createItem(request):
    form = ItemsForm()
    if request.method == 'POST':
        form =ItemsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form': form,
    }
    return render(request,template_name='create_item.html',context=context)

def updateItem(request,id):
    update =Items.objects.get(pk=id)
    form = ItemsForm(instance=update)
    if request.method == 'POST':
        form =ItemsForm(request.POST,request.FILES,instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, template_name='create_item.html', context=context)

def deleteItem(request,id):
    delete = Items.objects.get(pk=id)
    if request.method == "POST" :
        delete.delete()
        return redirect('/')
    context = {
        'item': delete,
    }
    return render(request, template_name='delete.html', context=context)







 # item_details page

def itemDetails(request, id):
    iDet = Items.objects.get( pk = id)
    context ={
        'iDetails':  iDet,
    }
    return render(request,template_name='item_details.html',context=context)


# products
def women(request):
    wo = ProductWomen.objects.all()
    context ={
        'won':  wo,
    }
    return render(request,template_name='women.html',context=context)


def womenDetails(request, id):
    wDet = ProductWomen.objects.get(pk = id)
    context ={
        'wDetails':  wDet,
    }
    return render(request,template_name='product_details_women.html',context=context)


def men(request):
    man = Men.objects.all()
    context ={
        'mann':  man,
    }
    return render(request,template_name='men.html',context=context)
def menDetails(request, id):
    mDet = Men.objects.get(pk = id)
    context ={
        'mDetails':  mDet,
    }
    return render(request,template_name='product_details_men.html',context=context)






# designer page
def designer(request):
    return render(request, template_name='designer.html')


# cart page
def cart(request):
    return render(request,template_name='cart.html')

# contact_us page
def contact(request):
    return render(request,template_name='contact_us.html')

