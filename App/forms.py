from django import forms
from App.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User 

class RegistroUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre')
    last_name = forms.CharField(max_length=20, label='Apellido')
    email = forms.EmailField()
    username = forms.CharField(max_length=15)
    password1 = forms.CharField(label='Contaseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Constraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username', 'password1', 'password2')

class NuevoBlog(forms.ModelForm):
    class Meta:
        model = NoticiaBlog
        fields = ['autor','categoriaN','encabezado','descripcion','email','imagenNoticias']

class EditarUsuario(UserChangeForm):
    first_name = forms.CharField(label='Nuevo nombre')
    last_name = forms.CharField(label='Nuevo apellido')
    username = forms.CharField(label='Nuevo username')
    email = forms.EmailField(label='Nuevo correo')
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email' )

class EditarPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña actual"), widget=forms.PasswordInput())
    new_password1 = forms.CharField(label=("Contraseña nueva"), widget=forms.PasswordInput())
    new_password2 = forms.CharField(label=("Contraseña nueva"), widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')