from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, "shop/shop.html")

def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            User = form.save()
            return redirect('/')
        else:
            return redirect('/shop/register')
    else:
        form = RegisterForm()
        
    return render(request, "shop/signup.html", {'form':form})