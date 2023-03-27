from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import NoticiaBlog

class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'App/index.html'

def register(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return render(request, "App/RegistroUsuario.html")
    else:
        form = RegistroUsuario()
    context = {'form':form}
    return render(request, "App/RegistroUsuario.html", context)

class NuevoBlogs(LoginRequiredMixin,CreateView):
    model = NoticiaBlog
    form_class = NuevoBlog
    success_url = reverse_lazy('App:Inicio')
    template_name = 'App/NuevoBlog.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NuevoBlogs, self).form_valid(form)

@login_required
def about(request):
    return render(request, 'App/index.html')

class editUser(LoginRequiredMixin, UpdateView):
    form_class = EditarUsuario
    template_name= 'App/EditarPerfil.html'
    success_url = reverse_lazy('App:Inicio')

    def get_object(self):
        return self.request.user

class editPass(LoginRequiredMixin, PasswordChangeView):
    form_class = EditarPassword
    template_name = 'App/EditarPassword.html'
    success_url = reverse_lazy('App:Inicio')

class mascotaLista(LoginRequiredMixin, ListView):
    context_object_name = 'mascotas'
    queryset = NoticiaBlog.objects.filter(categoriaN__startswith='mascotas')
    template_name = 'App/MascotaLista.html'

class mascotaDetalle(LoginRequiredMixin, DetailView):
    model = NoticiaBlog
    context_object_name = 'mascota'
    template_name = 'App/MascotaDetalle.html'

class mascotaUpdate(LoginRequiredMixin, UpdateView):
    model = NoticiaBlog
    form_class = NuevoBlog
    success_url = reverse_lazy('App:mascotas')
    context_object_name = 'mascota'
    template_name = 'App/MascotaEdicion.html'

class mascotaDelete(LoginRequiredMixin, DeleteView):
    model = NoticiaBlog
    success_url = reverse_lazy('App:mascotas')
    context_object_name = 'mascota'
    template_name = 'App/MascotaBorrado.html'

class viajeLista(LoginRequiredMixin, ListView):
    context_object_name = 'viajes'
    queryset = NoticiaBlog.objects.filter(categoriaN__startswith='viajes')
    template_name = 'App/ViajeLista.html'

class viajeDetalle(LoginRequiredMixin, DetailView):
    model = NoticiaBlog
    context_object_name = 'viaje'
    template_name = 'App/ViajeDetalle.html'

class viajeUpdate(LoginRequiredMixin, UpdateView):
    model = NoticiaBlog
    form_class = NuevoBlog
    success_url = reverse_lazy('App:viajes')
    context_object_name = 'viaje'
    template_name = 'App/ViajeEdicion.html'

class viajeDelete(LoginRequiredMixin, DeleteView):
    model = NoticiaBlog
    success_url = reverse_lazy('App:viajes')
    context_object_name = 'viaje'
    template_name = 'App/ViajeBorrado.html'

class entrenamientoLista(LoginRequiredMixin, ListView):
    context_object_name = 'entrenamientos'
    queryset = NoticiaBlog.objects.filter(categoriaN__startswith='entrenamiento')
    template_name = 'App/EntrenamientoLista.html'

class entrenamientoDetalle(LoginRequiredMixin, DetailView):
    model = NoticiaBlog
    context_object_name = 'entrenamiento'
    template_name = 'App/EntrenamientoDetalle.html'

class entrenamientoUpdate(LoginRequiredMixin, UpdateView):
    model = NoticiaBlog
    form_class = NuevoBlog
    success_url = reverse_lazy('App:entrenamientos')
    context_object_name = 'entrenamiento'
    template_name = 'App/EntrenamientoEdicion.html'

class entrenamientoDelete(LoginRequiredMixin, DeleteView):
    model = NoticiaBlog
    success_url = reverse_lazy('App:entrenamientos')
    context_object_name = 'entrenamiento'
    template_name = 'App/EntrenamientoBorrado.html'

class tecnologiaLista(LoginRequiredMixin, ListView):
    context_object_name = 'tecnologias'
    queryset = NoticiaBlog.objects.filter(categoriaN__startswith='tecnologia')
    template_name = 'App/TecnologiaLista.html'

class tecnologiaDetalle(LoginRequiredMixin, DetailView):
    model = NoticiaBlog
    context_object_name = 'tecnologia'
    template_name = 'App/TecnologiaDetalle.html'

class tecnologiaUpdate(LoginRequiredMixin, UpdateView):
    model = NoticiaBlog
    form_class = NuevoBlog
    success_url = reverse_lazy('App:tecnologias')
    context_object_name = 'tecnologia'
    template_name = 'App/TecnologiaEdicion.html'

class tecnologiaDelete(LoginRequiredMixin, DeleteView):
    model = NoticiaBlog
    success_url = reverse_lazy('App:tecnologias')
    context_object_name = 'tecnologia'
    template_name = 'App/TecnologiaBorrado.html'