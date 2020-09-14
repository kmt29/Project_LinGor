from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import *
import json
from django.http import HttpResponse, JsonResponse

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

def cart(request):
  
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    data = {'items' : items}
    return render(request, "shop/cart.html",data)

def updateItem(request):
    data =json.loads(request.body)
    itemID = data['id']
    action = data['action']

    customer = request.user.customer
    item = Item.objects.get(id=itemID)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,item=item)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    if action == 'remove':
        orderItem.quantity = orderItem.quantity + 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse("items been added to cart",safe=False)