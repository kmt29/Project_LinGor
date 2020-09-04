from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name="shop"),
    path('register',views.register,name="shop-register"),
    path('login',auth_views.LoginView.as_view(template_name="shop/signin.html"),name="shop-login"),
    path('logout',auth_views.LogoutView.as_view(template_name="shop/logout.html"),name="shop-lougout"),
]