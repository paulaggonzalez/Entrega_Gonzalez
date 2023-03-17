from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'App'
urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('register/',views.register, name='Register'),
    path('login/',LoginView.as_view(template_name='App/login.html'), name='Login'),
    path('logout/',LogoutView.as_view(template_name='App/logout.html'), name='Logout'),
    path('newblog/',views.nuevosBlog, name='Newblog'),
    path('editUser/',views.editUser.as_view(), name='EditUser'),
    path('editPass/',views.editPass.as_view(), name='EditPass'),
]