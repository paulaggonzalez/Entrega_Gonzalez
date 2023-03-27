from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'App'
urlpatterns = [
    path('', views.Inicio.as_view(), name='Inicio'),
    path('register', views.register, name='Register'),
    path('login/',LoginView.as_view(template_name='registration/login.html'), name='Login'),
    path('logout',LogoutView.as_view(template_name='App/logout.html'), name='Logout'),
    path('newblog',views.NuevoBlogs.as_view(), name='Newblog'),
    path('editUser',views.editUser.as_view(), name='EditUser'),
    path('editPass',views.editPass.as_view(), name='EditPass'),
    path('mascotaLista/', views.mascotaLista.as_view(), name='mascotas'),
    path('mascotaDetalle/<int:pk>/', views.mascotaDetalle.as_view(), name='mascota'),
    path('mascotaEdicion/<int:pk>/', views.mascotaUpdate.as_view(), name='Mascota_Edit'),
    path('mascotaBorrado/<int:pk>/', views.mascotaDelete.as_view(), name='Mascota_Delete'),
    path('viajeLista/', views.viajeLista.as_view(), name='viajes'),
    path('viajeDetalle/<int:pk>/', views.viajeDetalle.as_view(), name='viaje'),
    path('viajeEdicion/<int:pk>/', views.viajeUpdate.as_view(), name='Viaje_Edit'),
    path('viajeBorrado/<int:pk>/', views.viajeDelete.as_view(), name='Viaje_Delete'),
    path('entrenamientoLista/', views.entrenamientoLista.as_view(), name='entrenamientos'),
    path('entrenamientoDetalle/<int:pk>/', views.entrenamientoDetalle.as_view(), name='entrenamiento'),
    path('entrenamientoEdicion/<int:pk>/', views.entrenamientoUpdate.as_view(), name='Entrenamiento_Edit'),
    path('entrenamientoBorrado/<int:pk>/', views.entrenamientoDelete.as_view(), name='Entrenamiento_Delete'),
    path('tecnologiaLista/', views.tecnologiaLista.as_view(), name='tecnologias'),
    path('tecnologiaDetalle/<int:pk>/', views.tecnologiaDetalle.as_view(), name='tecnologia'),
    path('tecnologiaEdicion/<int:pk>/', views.tecnologiaUpdate.as_view(), name='Tecnologia_Edit'),
    path('tecnologiaBorrado/<int:pk>/', views.tecnologiaDelete.as_view(), name='Tecnologia_Delete'),

]