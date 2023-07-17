from . import views
from django.urls import path

urlpatterns = [
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('form',views.form,name='form')

    ]