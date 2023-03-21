from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'App'
urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('register', views.register, name='Register'),
    path('login/',LoginView.as_view(template_name='App/login.html'), name='Login'),
    path('logout',LogoutView.as_view(template_name='App/logout.html'), name='Logout'),
    path('newblog',views.NuevoBlogs.as_view(), name='Newblog'),
    path('editUser',views.editUser.as_view(), name='EditUser'),
    path('editPass',views.editPass.as_view(), name='EditPass'),
    path('mascotaLista/', views.mascotaLista.as_view(), name='mascotas'),
    path('mascotaDetalle/<int:pk>/', views.mascotaDetalle.as_view(), name='mascota'),
    path('mascotaEdicion/<int:pk>/', views.mascotaUpdate.as_view(), name='Mascota_Edit'),
    path('mascotaBorrado/<int:pk>/', views.mascotaDelete.as_view(), name='Mascota_Delete'),

]