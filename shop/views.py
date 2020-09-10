from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import *

# Create your views here.
def home(request):
    items = Item.objects.all()
    data = {'items' : items}
    return render(request, "shop/shop.html", data)

def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            User = form.save()
            return redirect('/shop/login')
        else:
            return redirect('/shop/login')
    else:
        form = RegisterForm()
        
    return render(request, "shop/signup.html", {'form':form})   