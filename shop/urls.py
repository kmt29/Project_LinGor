from . import views
from django.urls import path
urlpatterns = [
    path('',views.home,name="shop"),
    path('register',views.register,name="shop-register"),
]