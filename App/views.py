from django.shortcuts import render
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import NoticiaBlog

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

class NuevoBlogs(CreateView):
    model = NoticiaBlog
    form_class = NuevoBlog
    success_url = reverse_lazy('App:Inicio')
    template_name = 'App/NuevoBlog.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NuevoBlogs, self).form_valid(form)

def about(request):
    return render(request, 'App/index.html')

class editUser(UpdateView):
    form_class = EditarUsuario
    template_name= 'App/EditarPerfil.html'
    success_url = reverse_lazy('App:Inicio')

    def get_object(self):
        return self.request.user

class editPass(PasswordChangeView):
    form_class = EditarPassword
    template_name = 'App/EditarPassword.html'
    success_url = reverse_lazy('App:Inicio')

class mascotaLista(ListView):
    context_object_name = 'mascotas'
    queryset = NoticiaBlog.objects.filter(categoriaN__startswith='mascotas')
    template_name = 'App/MascotaLista.html'

class mascotaDetalle(DetailView):
    model = NoticiaBlog
    context_object_name = 'mascotas'
    template_name = 'App/MascotaDetalle.html'

class mascotaUpdate(UpdateView):
    model = NoticiaBlog
    form_class = NuevoBlog
    success_url = reverse_lazy('mascotas')
    context_object_name = 'mascota'
    template_name = 'App/MascotaEdicion.html'

class mascotaDelete(DeleteView):
    model = NoticiaBlog
    success_url = reverse_lazy('mascotas')
    context_object_name = 'mascota'
    template_name = 'App/MascotaBorrado.html'