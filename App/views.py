from django.shortcuts import render
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def inicio (request):
    return render(request, "App/index.html")

def register(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return render(request, "App/index.html")
    else:
        form = RegistroUsuario()
    context = {'form':form}
    return render(request, "App/RegistroUsuario.html", context)

def nuevosBlog(request):
    if request.method == 'POST':
        formulario = NuevoBlog(request.POST)
        if formulario.is_valid():
            formulario.save()
            newblog = formulario.cleaned_data['newblog']
            return render(request, "App/index.html")
    else:
        formulario = NuevoBlog()
    context = {'formulario':formulario}
    return render(request, "App/NuevoBlog.html", context)

def about(request):
    return render(request, 'App/index.html')

class editUser(UpdateView):
    form_class = EditarUsuario
    template_name= 'App/EditarPerfil.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self):
        return self.request.user

class editPass(PasswordChangeView):
    form_class = EditarPassword
    template_name = 'App/EditarPassword.html'
    success_url = reverse_lazy('Inicio')