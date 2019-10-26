from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
from .models import Bem
from django.utils import timezone
from .forms import BemForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class BemListView(ListView):
    model = Bem

    def get_queryset(self):
        return Bem.objects.filter(dataPreenchimento__lte=timezone.now()).order_by('-dataPreenchimento')

class BemDetailView(DetailView):
    model = Bem

class CreateBemView(CreateView):
    # login_url = '/login/'
    redirect_field_name = 'bem/bem_detalhe.html'

    form_class = BemForm
    model = Bem

class BemUpdateView(UpdateView):
    # login_url = '/login/'
    redirect_field_name = 'bem/bem_detalhe.html'

    form_class = BemForm

    model = Bem

class BemDeleteView(DeleteView):
    model = Bem
    success_url = reverse_lazy('gest_patr:bens_lista')
