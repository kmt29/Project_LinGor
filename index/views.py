from django.shortcuts import render
from django.http import request

# Create your views here.
def index(request):
    return render(request,"index/index.html")

def about(request):
    return render(request,"index/about.html")
