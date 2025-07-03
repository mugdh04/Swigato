from django.shortcuts import render, HttpResponse, redirect
from .models import Restaurant, Contact_Query, MenuItem
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import process_message
from.models import MenuItem, Product

def home(request):
    return render(request,'test1/home2.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'test1/loginuser.html', {'form':AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username=a, password=b)
        if user is None:
            return render(request,'test1/loginuser.html', {'form':AuthenticationForm(), 'error':'Invalid Credentials'})
        else:
            login(request, user)
            return redirect('home')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'test1/signupuser.html', {'form':UserCreationForm()})   
    else:
        a = request.POST.get('username')
        b = request.POST.get('password1')
        c = request.POST.get('password2')
        if b==c:
                # check whether user name is unique
            if (User.objects.filter(username = a)):
                return render(request,'test1/signupuser.html', {'form':UserCreationForm(), 'error':'User Name already exists! Try again with different username'})
            else:
                user = User.objects.create_user(username = a, password=b)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            # password 1 and 2 do not match
            return render(request,'test1/signupuser.html', {'form':UserCreationForm(), 'error':'Password Mismatch! Try again'})   

def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')
  
def order_online(request):
    return render(request,'test1/order_online.html')

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    return render(request, 'test1/restaurant.html', {'restaurant': restaurant, 'menu_items': menu_items})

def categorize_food_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            products, answer = process_message(message)
            if products:
                return render(request, 'test1/products.html', {'products': products, 'answer': answer})
            else:
                return HttpResponse("An error occurred while processing your request.")
    return render(request, 'test1/products.html')

def bite(request):
    return render(request,'test1/ai.html')
