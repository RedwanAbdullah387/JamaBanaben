from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ItemsForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@unauthenticated_user
def Registration(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, "Account was created for " + username)
            return redirect('loginPage')

    context = {
        'form': form,
    }
    return render(request, template_name='Registration.html', context=context)


@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password incorrect")

    context = {

    }
    return render(request, template_name='login.html', context=context)


def logoutuser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
@admin_only
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

def updateItem(request,pk):
    update =Items.objects.get(id=pk)
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

def deleteItem(request,pk):
    delete = Items.objects.get(id=pk)
    if request.method == "POST":
        delete.delete()
        return redirect('/')
    context = {
        'item': delete,
    }
    return render(request, template_name='delete.html', context=context)







 # item_details page

def itemDetails(request, pk):
    iDet = Items.objects.get(id=pk)
    context ={
        'iDetails':  iDet,
    }
    return render(request,template_name='item_details.html',context=context)


# products

# @login_required(login_url='login')
def women(request):
    wo = ProductWomen.objects.all()
    context ={
        'won':  wo,
    }
    return render(request,template_name='women.html',context=context)


def womenDetails(request, pk):
    wDet = ProductWomen.objects.get(id=pk)
    context ={
        'wDetails':  wDet,
    }
    return render(request,template_name='product_details_women.html',context=context)

# @login_required(login_url='login')
def men(request):
    man = Men.objects.all()
    context ={
        'mann':  man,
    }
    return render(request,template_name='men.html',context=context)
def MenDetails(request, pk):
    mDet =Men.objects.get(id=pk)
    context ={
        'm_Details':  mDet,
    }
    return render(request,template_name='product_details_men.html',context=context)






# designer page
def designer(request):
    return render(request, template_name='designer.html')


# cart page
@login_required(login_url='login')
def cart(request):
    return render(request,template_name='cart.html')

# contact_us page
def contact(request):
    return render(request,template_name='contact_us.html')

@login_required(login_url='loginPage')
#coustomer
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    items = Items.objects.all()
    context = {
        'item': items,
    }

    return render(request,template_name='user.html',context=context)

